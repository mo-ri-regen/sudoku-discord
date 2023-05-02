import random

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True

    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    return False

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def generate_puzzle(num_blanks):
    # Create a fully solved Sudoku board
    board = [[0 for _ in range(9)] for _ in range(9)]
    while not solve(board):
        for i in range(9):
            for j in range(9):
                board[i][j] = random.randint(1, 9)

    # Mask the specified number of cells to create the puzzle
    for _ in range(num_blanks):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0

    return board

def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
            if j in [2, 5]:
                print("|", end=" ")
        print()
        if i in [2, 5]:
            print("-" * 21)

if __name__ == "__main__":

    num_blanks = 40  # Number of blank cells in the puzzle
    puzzle = generate_puzzle(num_blanks)
    print_board(puzzle)
