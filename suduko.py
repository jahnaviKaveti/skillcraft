import random

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def generate_sudoku():
    board = [[0] * 9 for _ in range(9)]
    for _ in range(17):  # Minimum clues for a unique solution
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while not is_valid(board, row, col, num) or board[row][col] != 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
        board[row][col] = num
    solve_sudoku(board)
    return board
def play_sudoku():
    board = generate_sudoku()
    print("Welcome to Sudoku!")
    print_board(board)

    while True:
        try:
            row = int(input("Enter row (0-8) or -1 to quit: "))
            if row == -1:
                print("Thanks for playing!")
                break
            col = int(input("Enter column (0-8): "))
            num = int(input("Enter number (1-9): "))

            if is_valid(board, row, col, num):
                board[row][col] = num
                print_board(board)
                if all(all(num != 0 for num in row) for row in board):
                    print("Congratulations! You've completed the Sudoku!")
                    break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0-8 for row and column, and 1-9 for number.")

if __name__ == "__main__":
    play_sudoku()