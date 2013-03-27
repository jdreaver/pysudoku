from solver import *
from time import time

puzzles = loadfile()
possibs = [convert_puzzle(puzzle) for puzzle in puzzles]

a = time()
sum = 0
for i,p in enumerate(possibs):
    ans = logic_solve(p)
    sum += int(ans['A1'] + ans['A2'] + ans['A3'])

print "Time:", time() - a, "seconds"
print "Answer:", sum
