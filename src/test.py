#!/usr/bin/env python3

import unittest

from Sudoku import Sudoku

class Test_Sudoku(unittest.TestCase):
    
    def setUp(self):
        self.sudoku = Sudoku()
    
    def test_zero_grid(self):
        grid = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9],[4, 5, 6, 7, 8, 9, 1, 2, 3],[7, 8, 9, 1, 2, 3, 4, 5, 6],[2, 1, 4, 3, 6, 5, 8, 9, 7],[3, 6, 5, 8, 9, 7, 2, 1, 4],[8, 9, 7, 2, 1, 4, 3, 6, 5],[5, 3, 1, 6, 4, 2, 9, 7, 8],[6, 4, 2, 9, 7, 8, 5, 3, 1],[9, 7, 8, 5, 3, 1, 6, 4, 2],]
        
        self.sudoku.load_grid(grid)
        self.sudoku.solve()
        assert self.sudoku.grid == expected
       
    def test_special_grid(self):
        # http://www.mathematische-basteleien.de/sudoku.htm
        grid = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
        expected = [[5, 3, 4, 6, 7, 8, 9, 1, 2],[6, 7, 2, 1, 9, 5, 3, 4, 8],[1, 9, 8, 3, 4, 2, 5, 6, 7],[8, 5, 9, 7, 6, 1, 4, 2, 3],[4, 2, 6, 8, 5, 3, 7, 9, 1],[7, 1, 3, 9, 2, 4, 8, 5, 6],[9, 6, 1, 5, 3, 7, 2, 8, 4],[2, 8, 7, 4, 1, 9, 6, 3, 5],[3, 4, 5, 2, 8, 6, 1, 7, 9]]
        self.sudoku.load_grid(grid)
        self.sudoku.solve()
        assert self.sudoku.grid == expected 
        
    def test_exteme_grid(self):
        # http://www.mathematische-basteleien.de/sudoku.htm
        grid = [[0,0,9,0,0,0,8,0,0],[0,1,0,3,0,7,0,9,0],[5,0,0,0,0,0,0,0,4],[0,3,0,4,0,2,0,8,0],[0,0,0,0,3,0,0,0,0],[0,6,0,9,0,1,0,7,0],[8,0,0,0,0,0,0,0,6],[0,2,0,5,0,6,0,1,0],[0,0,3,0,0,0,5,0,0]] 
        expected = [[3, 7, 9, 2, 4, 5, 8, 6, 1],[4, 1, 6, 3, 8, 7, 2, 9, 5],[5, 8, 2, 1, 6, 9, 7, 3, 4],[1, 3, 5, 4, 7, 2, 6, 8, 9],[9, 4, 7, 6, 3, 8, 1, 5, 2],[2, 6, 8, 9, 5, 1, 4, 7, 3],[8, 5, 1, 7, 2, 3, 9, 4, 6],[7, 2, 4, 5, 9, 6, 3, 1, 8],[6, 9, 3, 8, 1, 4, 5, 2, 7]]
        self.sudoku.load_grid(grid)
        self.sudoku.solve()
        assert self.sudoku.grid == expected
        
        
        
if __name__ == "__main__":
    unittest.main() # run all tests