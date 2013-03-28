import solver

euler_file = 'euler_sudokus.txt'
search_puzzle = '400000805030000000000700000020000060000080400000010000000603070500200000104000000'
search_solution = '417369825632158947958724316825437169791586432346912758289643571573291684164875293'


def test_utilities():
    assert len(solver.cells) == 81
    assert len(solver.squares) == 9

def test_simple_constraints():
    assert solver.propagate_constraints('1', {'A1':'1'}, ['A1']) == False
    assert solver.propagate_constraints('1', {'A1':'234'}, ['A1']) == True

def test_load_parser():
    simple = '123456789'*9
    funky = """12345678.123456789123456789|123*456/7..
               1234%^&567891||23456789123/?/?456789123456789123456789"""
    grid = """4 . . |. . . |8 . 5     
              . 3 . |. . . |. . .     
              . . . |7 . . |. . .     
              ------+------+------    
              . 2 . |. . . |. 6 .     
              . . . |. 8 . |4 . .     
              . . . |. 1 . |. . .     
              ------+------+------    
              . . . |6 . 3 |. 7 .     
              5 . . |2 . . |. . .     
              1 . 4 |. . . |. . .     """

    parsed = solver.parse_sudokus(simple+funky+grid, unknown_value='.')
    assert len(parsed) == 3
    assert all([len(puzzle) == 81 for puzzle in parsed])

def test_search_solve():
    solution = solver.solve_puzzle(search_puzzle)
    str_solution = solver.convert_solution(solution)
    assert str_solution == search_solution
