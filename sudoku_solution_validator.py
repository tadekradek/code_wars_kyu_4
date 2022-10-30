"""
Sudoku Background

Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)
Sudoku Solution Validator

Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
Examples

validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true

validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]); // => false

"""
#my solution (seems to be preety fine)

def valid_solution(board):
    #condition of all rows
    def rows(board):
        for x in board: 
            if sorted(x) != [1,2,3,4,5,6,7,8,9]:
                return False

    #condition of all columns
    def columns(board):
        for y in range (0,9):
            if sorted([board[x][y] for x in range(0,9)]) != [1,2,3,4,5,6,7,8,9]:
                return False


    #condition of all blocks
    def blocks(board):
        for x in range (0,9,3):
            for y in range (0,9,3):
                if sorted([board[x][y+z] for z in range(0,3)] + [board[x+1][y+z] for z in range(0,3)] + [board[x+2][y+z] for z in range(0,3)]) != [1,2,3,4,5,6,7,8,9]:
                    return False


    if rows(board) == False or columns(board) == False or blocks(board) == False:
        return False
    else:
        return True

#another solutions

correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def validSolution(board):
    # check rows
    for row in board:
        if sorted(row) != correct:
            return False
    
    # check columns
    for column in zip(*board):
        if sorted(column) != correct:
            return False
    
    # check regions
    for i in range(3):
        for j in range(3):
            region = []
            for line in board[i*3:(i+1)*3]:
                region += line[j*3:(j+1)*3]
            
            if sorted(region) != correct:
                return False
    
    # if everything correct
    return True


###

def validSolution (board):
    valid = set(range(1, 10))
    
    for row in board:
        if set(row) != valid: return False
    
    for col in [[row[i] for row in board] for i in range(9)]:
        if set(col) != valid: return False
    
    for x in range(3):
        for y in range(3):
            if set(sum([row[x*3:(x+1)*3] for row in board[y*3:(y+1)*3]], [])) != valid:
                return False
    
    return True

