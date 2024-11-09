# Import the system and random modules to use system commands and random functions
import os
import random

# Function to display the Tic-Tac-Toe board
def print_board(board):
    os.system('clear')  # Clear the console for better readability
    print("Tic Tac Toe")
    print("-----------")
    # Loop through each row and display the board
    for row in range(3):
        print(" | ".join(board[row]))  # Print each cell separated by a vertical line
        if row < 2:
            print("---------")  # Print a horizontal line between rows

# Function to check if there's a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals for a winning combination
    for row in range(3):
        if all(cell == player for cell in board[row]):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full (for a tie)
def is_full(board):
    # Loop through each cell, return False if an empty cell is found
    return all(cell != " " for row in board for cell in row)

# Function to get a player's move
def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1  # Get move, subtract 1 for 0-index
            row, col = divmod(move, 3)  # Convert move to row and column
            # Check if the cell is empty
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell is not empty!")
        except (ValueError, IndexError):
            print("Invalid move. Enter a number between 1 and 9.")

# Function for the computer's move
def get_computer_move(board):
    # Generate random moves until an empty cell is found
    while True:
        move = random.randint(0, 8)
        row, col = divmod(move, 3)
        if board[row][col] == " ":
            return row, col

# Main function to play the game
def play_game():
    # Initialize an empty 3x3 board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Set the starting player

    while True:
        print_board(board)  # Display the board
        if current_player == "X":
            print("Player's Turn")
            row, col = get_player_move(board)  # Get player's move
        else:
            print("Computer's Turn")
            row, col = get_computer_move(board)  # Get computer's move

        board[row][col] = current_player  # Mark the move on the board

        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break

        # Check if the board is full (tie)
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()                                                                                                                                   