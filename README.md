#pysudoku

This is a sudoku solver I made in python. 

#Sudoku

According to [Wikipedia](http://en.wikipedia.org/wiki/Sudoku):

    *Sudoku*, originally called Number Place, is a logic-based,
    combinatorial number-placement puzzle. The objective is to fill a
    9×9 grid with digits so that each column, each row, and each of
    the nine 3×3 sub-grids that compose the grid (also called "boxes",
    "blocks", "regions", or "sub-squares") contains all of the digits
    from 1 to 9. The puzzle setter provides a partially completed
    grid, which typically has a unique solution.

Here is in example:

![Unsolved sudoku](/img/unsolved.png)

![Solved sudoku](/img/solved.png)

#Solution

This solver consists of two parts: constraint propagation and a search.
