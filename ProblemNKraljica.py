def is_safe(board, row, col, N):
    # Checking if queens are attacked
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True

def solve_n_queens(board, row, N):
    # base case, all queens are set
    if row == N:
        return True
    
    for col in range(N):
        # checking if position is safe
        if is_safe(board, row, col, N):
            board[row][col] = 1
            # recursively calling out function for setting next queens
            if solve_n_queens(board, row+1, N):
                return True
            # going back if queen can't be set
            board[row][col] = 0
    
    # Returning false if queen can't be set
    return False

def print_board(board):
    for row in board:
        print(row)

def solve_n_queens_main(N):
    board = [[0 for x in range(N)] for y in range(N)]
    if solve_n_queens(board, 0, N):
        print_board(board)
    else:
        print("No solution")
        
solve_n_queens_main(8)