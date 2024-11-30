from collections import defaultdict
def isValidSudoku( board):
    rows = defaultdict(set) # the key is the index and the value is set of element of the row or col
    cols = defaultdict(set)
    squares = defaultdict(set) # the key is (r//3, c//3)
    
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3 , c//3)] ):
                return False
            
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3,c//3)].add(board[r][c])
            
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))

"""
time complexity is O(n2) for rows and cols 

for space O(n) for rows and cols and O(k2) for squares, k is the size of the sub-box ->3

i advice to see the other solution improves the space also the explanation of the time and space comp
"""
