from Sudoku import Sudoku

grid0 = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
       ]

grid1 = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
       ]

grid2 = [
        [0,0,9,0,0,0,8,0,0],
        [0,1,0,3,0,7,0,9,0],
        [5,0,0,0,0,0,0,0,4],
        [0,3,0,4,0,2,0,8,0],
        [0,0,0,0,3,0,0,0,0],
        [0,6,0,9,0,1,0,7,0],
        [8,0,0,0,0,0,0,0,6],
        [0,2,0,5,0,6,0,1,0],
        [0,0,3,0,0,0,5,0,0]
       ]


def main (grid):
    solve(grid)
    show(grid)
    
def show (grid):
    for i in range(9):
        print (grid[i])

def solve (grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        y,x = find
        
    for value in range(1,10):
        if is_possible(grid, y, x, value):
            grid[y][x] = value
            
            if solve(grid):
                return True
            
            grid[y][x] = 0
            
    return False
                

def find_empty(grid):
    for y in range (len(grid)):
        for x in range (len(grid[y])):
            if grid[y][x] == 0:
                return (y,x)
    return None
  
def is_possible(grid, y,x, value):
    return check_line(grid, y,x, value) and check_row(grid, y, x, value) and check_square(grid, y, x, value)
        
def check_line(grid, y,x, value):
    for i in range (len(grid[y])):
        if grid[y][i] == value and i != x:
            return False        
    return True

def check_row(grid, y,x, value):
    for i in range (len(grid)):
        if grid[i][x] == value and i != y:
            return False        
    return True

def check_square(grid, y,x, value):
    s_y = y // 3
    s_x = x // 3
    for i in range(s_y*3, s_y*3 +3):
        for j in range (s_x*3, s_x*3 +3):
            if grid[i][j] == value and (i,y) != (y,x):
                return False    
    return True



#main (grid0.copy())

s = Sudoku(grid2.copy())
s.solve()
show (s.grid)















