


class Sudoku:
    def __init__(self, grid = None):
        self.grid = grid
        
        self.load_grid(grid)
         
    def solve(self):
        return self._solve()
    
    def load_grid(self, grid):
        if grid:
            self.grid = grid
            self.y_len = len(self.grid)
            self.x_len = len(self.grid[0])    # assuming it's a square grid
                   
    def _solve(self):
        pos = self.find_empty()
        if not pos:
            return True
        else:
            y,x = pos 
        
        for value in range(1,10):
            if self.is_possible(value, y, x):
                self.grid[y][x] = value
            
                if self._solve():
                    return True
                
                self.grid[y][x] = 0 #reset
            
        return False
        
    def find_empty(self):
        for y in range(self.y_len):
            for x in range(self.x_len):
                if self.grid[y][x] == 0:
                    return (y,x)
        return None
            
    def is_possible(self, value, y,x):
        return self._check_line(value, y, x) and self._check_row(value, y, x) and self._check_square(value, y, x)
    
    def _check_square(self, value, y,x):
        s_y = y // 3
        s_x = x // 3
        for i in range(s_y*3, s_y*3 +3):
            for j in range (s_x*3, s_x*3 +3):
                if self.grid[i][j] == value and (i,y) != (y,x):
                    return False  
        
        return True
    
    def _check_line(self, value, y,x):
        for i in range (self.x_len):
            if self.grid[y][i] == value and i != x:
                return False
        
        return True
    
    def _check_row(self, value, y,x):
        for i in range (self.y_len):
            if self.grid[i][x] == value and i != y:
                return False
        
        return True
