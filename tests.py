from solver import *

def test_utilities():
    assert len(cells) == 81
    assert len(squares) == 9

    assert len(puzzles) == 50
    assert len(puzzles[0]) == 81

    assert propagate_constraints('1', {'A1':'1'}, ['A1']) == False
    assert propagate_constraints('1', {'A1':'234'}, ['A1']) == True
