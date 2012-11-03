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


