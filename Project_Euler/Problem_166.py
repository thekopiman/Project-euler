#!/usr/bin/env python3
'''
A 4x4 grid is filled with digits d, 0 ≤ d ≤ 9.

It can be seen that in the grid

6 3 3 0
5 0 4 3
0 7 1 4
1 2 4 5

the sum of each row and each column has the value 12. Moreover the sum of each diagonal is also 12.

In how many ways can you fill a 4x4 grid with the digits d, 0 ≤ d ≤ 9 so that each row, each column, and both diagonals have the same sum?
'''

import numpy as np

empty_grid = np.zeros([4,4], dtype=np.int16)

class CrissCross():
    def __init__(self, grid = None):
        self.grid = grid

    def axial(self, grid = None, coordinate):
        if grid == None:
            grid = self.grid
        
        for x in range(4):
            pass
        
    




print(empty_grid)