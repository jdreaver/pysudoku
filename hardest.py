from solver import *
from time import time

hardest = '000006000059000008200008000045000000003000000006003054000325006000000000000000000'

poss = convert_puzzle(hardest)

a = time()
display(logic_solve(poss))
print "Time: ", time() - a
