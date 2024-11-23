# Tic-Tac-Toe Board Representation
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Constants for player symbols
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to print the current state of the board
def print_board():
    for row in board:
        print('|'.join(row))
        print('-----')

# Function to check if the current player has won
def is_winner(player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full():
    return all(board[i][j] != EMPTY for i in range(3) for j in range(3))

# Function to evaluate the board for Mini-Max algorithm
def evaluate_board():
    if is_winner(PLAYER_X):
        return 1
    elif is_winner(PLAYER_O):
        return -1
    elif is_board_full():
        return 0
    else:
        return None

# Mini-Max Algorithm
def minimax(depth, is_maximizing):
    score = evaluate_board()

    if score is not None:
        return score

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    score = minimax(depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    score = minimax(depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

# Function to find the best move for the AI
def find_best_move():
    best_score = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                score = minimax(0, False)
                board[i][j] = EMPTY

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

# Function to play the game
def play_game():
    while True:
        print_board()

        # Player's move
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))

        if board[row][col] != EMPTY:
            print("Cell already occupied. Try again.")
            continue

        board[row][col] = PLAYER_O

        # Check if player wins
        if is_winner(PLAYER_O):
            print_board()
            print("Player (O) wins!")
            break

        # Check for a tie
        if is_board_full():
            print_board()
            print("It's a tie!")
            break

        print_board()

        # AI's move
        print("AI's move:")
        best_move = find_best_move()
        board[best_move[0]][best_move[1]] = PLAYER_X

        # Check if AI wins
        if is_winner(PLAYER_X):
            print_board()
            print("AI (X) wins!")
            break

        # Check for a tie
        if is_board_full():
            print_board()
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()