# Load utility functions

def loadfile():
    '''Load sudokus as one line string.'''
    sudokus = []
    with open('sudoku.txt', 'r') as f:
        for i, line in enumerate(f):
            if i % 10 == 0:
                puzzle = ''
            else:
                puzzle += line.rstrip()
            if i % 10 == 9:
                sudokus.append(puzzle)
    return sudokus
