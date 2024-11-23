# Function to check if a queen can be placed on board[row][col]
def is_safe(board, row, col, n):
    # Check this column on the upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


# Function to solve the N-Queens problem using backtracking
def solve_n_queens(board, row, n):
    # If all queens are placed, return True
    if row >= n:
        return True

    # Try placing a queen in all columns one by one
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row][col] = 1

            # Recur to place the rest of the queens
            if solve_n_queens(board, row + 1, n):
                return True

            # If placing queen in board[row][col] leads to failure, remove the queen
            board[row][col] = 0

    return False


# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))


# Main function to set up the board and solve the problem
def main():
    n = 8  # Number of queens (size of the chessboard)
    board = [[0] * n for _ in range(n)]  # Initialize the board

    if solve_n_queens(board, 0, n):
        print("Solution for the 8-Queens problem:")
        print_board(board)
    else:
        print("No solution exists")


if __name__ == "__main__":
    main()
