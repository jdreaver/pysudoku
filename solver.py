from load_sudokus import *

# Sudoku solver

def cross(A, B):
    return [a + b for a in A for b in B]

letters = 'ABCDEFGHI'
numbers = '123456789'

cells = cross(letters, numbers)
rows = [cross(letter, numbers) for letter in letters]
columns = [cross(letters, num) for num in numbers]
squares = [cross(lets, nums) 
           for lets in ('ABC', 'DEF', 'GHI') for nums in ('123', '456', '789')]
unitlist = rows + columns + squares

units = dict((c, [unit for unit in unitlist if c in unit]) for c in cells)
peers = dict((c, set(sum(units[c],[])) - set([c])) for c in cells)

# Create puzzles

puzzles = loadfile()

def convert_puzzle(puzzle):
    possibs = {}
    for i, cell in enumerate(cells):
        possibs[cell] = numbers if puzzle[i] == '0' else puzzle[i]
    return possibs

possibs = [convert_puzzle(puzzle) for puzzle in puzzles]

# Logic Solver
def remove_from_string(string, value):
    '''Removes value from string if it is in string, else does nothing'''
    loc = string.find(value)
    if loc > -1:
        string = string[:loc] + string[loc + 1:]

def propagate_constraints(value, possibs, peers):
    for peer in peers:
        loc = possibs[peer].find(value)
        if loc > -1:
            possibs[peer] = possibs[peer][:loc] + possibs[peer][loc + 1:] 
            

def logic_solve(possibs):
    unsolved_cells = [k for k in possibs.keys()]
    num_changed = 1
    while num_changed > 0:
        num_changed = 0
        for i, cell in enumerate(unsolved_cells):
            value = possibs[cell]
            if len(value) == 1:
                del unsolved_cells[i]
                propagate_constraints(value, possibs, peers[cell])
                num_changed += 1
    #return possibs
    return search_solve(possibs, unsolved_cells) if unsolved_cells else possibs

# Search
def check_constraint(value, possibs, peers):
    return all([value != possibs[peer] for peer in peers if len(possibs[peer]) == 1])

def search_solve(possibs, unsolved_cells):
    N = len(unsolved_cells)
    poss_fillins = dict((cell, possibs[cell]) for cell in unsolved_cells)
    i = 0
    #while i < N:
    #    possibs[cell] = 
        

# Display function (stolen from Norvig)
def display(values):
    "Display these values as a 2-D grid."
    width = 1+max(len(values[c]) for c in cells)
    line = '+'.join(['-'*(width*3)]*3)
    for r in letters:
        print ''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in numbers)
        if r in 'CF': print line
    print

