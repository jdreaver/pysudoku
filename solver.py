"""
Main solving routines for a loaded sudoku.
"""

## Board Setup and Utilities (taken from Norvig)
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

def convert_puzzle(puzzle):
    possibs = {}
    for i, cell in enumerate(cells):
        possibs[cell] = numbers if puzzle[i] == '0' else puzzle[i]
    return possibs

## Main solving function
def solve_puzzle(puzzle):

    """Solves sudoku using two step method.

    Given a sudoku puzzle string, this function returns an output
    string with all missing values filled in.

    Args:
        puzzle: one-line string representing an unsolved puzzle

    Returns:
        One-line string with missing values filled in, or None if 
        there is no solution.

    """

    possibilities = convert_puzzle(puzzle)
    (solution, unsolved_cells) = logic_solve(possibilities)
    if unsolved_cells:
        solution = search_solve(possibilities, unsolved_cells)
    return solution
        

def convert_solution(solution):
    
    """Turns solution dictionary into string."""

    return ''.join([value for cell, value in sorted(solution.items())])

## Logic Solver

def propagate_constraints(value, possibs, cell_peers):
    for peer in cell_peers:
        loc = possibs[peer].find(value)
        if possibs[peer] == value:
            return False
        if loc > -1:
            possibs[peer] = possibs[peer][:loc] + possibs[peer][loc + 1:]
    return True
            

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
    return (possibs, unsolved_cells)

# Search
# def check_constraint(value, possibs, peers):
#     return all([value != possibs[peer] for peer in peers if len(possibs[peer]) == 1])
        

def search_solve(possibs, unsolved_cells):
    unsolved_cells = sorted(unsolved_cells, key=lambda c: len(possibs[c]))
    node = (possibs, unsolved_cells)
    frontier = [node]
    while frontier:
        node = frontier.pop()
        if not node[1]:
            return node[0]
        children = generate_children(node)
        frontier.extend(children)
    return None

def generate_children(node):
    children = []
    (possibs, unsolved_cells) = node
    cell = unsolved_cells[0]
    for val in possibs[cell]:
        new_possibs = possibs.copy()
        if propagate_constraints(val, new_possibs, peers[cell]):
            new_possibs[cell] = val
            #print cell
            #display(new_possibs)
            new_unsolved_cells = unsolved_cells[1:]
            children.append((new_possibs, new_unsolved_cells))
    return children

# Display function (taken from Norvig)
def display(values):
    "Display these values as a 2-D grid."
    width = 1+max(len(values[c]) for c in cells)
    line = '+'.join(['-'*(width*3)]*3)
    for r in letters:
        print ''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in numbers)
        if r in 'CF': print line
    print


def string_display(puzzle):
    lines = [puzzle[9*i:9*(i+1)] for i in range(9)]
    separator = '+' + '+'.join(['---']*3) + '+'
    for i, line in enumerate(lines):
        if i % 3 == 0:
            print separator
        this_line = ''.join(c + ('|' if str(i) in '25' else '')
                            for i, c in enumerate(line))
        this_line = '|' + this_line + '|'
        print this_line
    print separator
            
    


# Check Sudoku
def check(possibs):
    for c in cells:
        val = possibs[c]
        for p in [k for peer in peers[c] for k in possibs[peer]]:
            if p == val:
                return False
    return True

# Load utility functions
def parse_sudokus(raw_string, unknown_value='.'):
    """Converts one or more puzzles into single-line strings.

    This function takes a series of sudokus and converts them into
    seperate one-line strings. This is done by first replacing all
    instances of the unknown_value with 0, and then removing everything
    but integers in raw_string. Each set of 81 consecutive integers
    constitutes one puzzle. 

    This means that a user's representation of puzzles can have all
    manner of decorations as long as integers and the representation
    of unknown values are consecutive when read from left to right,
    top to bottom. 

    Args:
        raw_string: one or more raw puzzles in a string
        unknown_value: user's representation of unknown value
    
    Returns:
        A list of single-line, length 81 strings of integers

    """
    
    replaced = raw_string.replace(unknown_value, '0')
    digits = ''.join((x for x in replaced if x.isdigit()))
    if len(digits) % 81 != 0:
        print "Not a proper number of digits in string!"
        return None

    puzzles = [digits[81*i:81*(i+1)] for i in range(len(digits)/81)]
    return puzzles

# def load_file(filename):
#     with open(filename) as f:
#         return f.read()

# def loadfile():
#     '''Load sudokus as one line string.'''
#     sudokus = []
#     with open('sudoku.txt', 'r') as f:
#         for i, line in enumerate(f):
#             if i % 10 == 0:
#                 puzzle = ''
#             else:
#                 puzzle += line.rstrip()
#             if i % 10 == 9:
#                 sudokus.append(puzzle)
#     return sudokus
