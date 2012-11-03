from solver import *
from load_sudokus import *

def test_suite():
    assert len(cells) == 81
    assert len(squares) == 9

    puzzles = loadfile()
    assert len(puzzles) == 50
    assert len(puzzles[0]) == 81
