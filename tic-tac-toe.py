    """
    Filename: tic-tac-toe.py
    Author: Benjamin McKee

    Description:
    ------------
    This is a terminal-based Tic Tac Toe game written in Python.
    Players can choose to play against another person (2-player mode) or against a simple AI opponent (1-player mode).

    This game displays a 3x3 grid, accepts moves via terminal input (1-9), and determines a win or draw based on standard Tic Tac Toe rules.

    Features:
    - Clear terminal board display
    - Input validation
    - Simple AI opponent (random move selection)
    - Win and draw detection
    - Replay-friendly structure

    Instructions:
    -------------
    - Run the program in a terminal using: `python tic-tac-toe.py`
    - Follow prompts to select game mode and input moves
    - Moves are entered using numbers 1-9 corresponding to the board:

         1 | 2 | 3
        ---+---+---
         4 | 5 | 6
        ---+---+---
         7 | 8 | 9
    """

import random
import os
import platform

# Utility Functions

def clear_screen():
    # Clears terminal screen for better readability based on OS
    if platform.system() = "Windows":
        os.system("cls")
    else:
        os.system("clear")

def print_board(board):
    # Displays current state of the Tic Tac Toe board
    print()
    for i in range(3):
        row = " | ".join(board[i*3]:(i+1)*3])
        print(" " + row)
        if i < 2:
            print("---+---+---")
    print()

def check_win(board, player):
    # Checks if a player has won the game
    # Add win condition checks
    pass

def check_draw(board):
    # Checks if board is full and it is a draw
    # Return true if no empty space and no winner
    pass

def switch_player(current):
    # Switch player between X and O
    return 'O' if current == 'X' else 'X'

# Move Handling

def get_player_move(board, player):
    # Gets and applies move from human player
    while True:
        move = input(f"Player {player}, enter your move (1-9): ")
        if move.isdigit():
            index = int(move) - 1
            if 0 <= index < 9 and board[index] == ' ':
                board[index] = player
                break
        print("Invalid move. Try again.")

def get_ai_move(board):
    # Simple AI chooses random spot on the board
    print("AI is thinking...")
    available = [i for i, spot in enumerate(board) if spot == ' ']
    if available:
        index = random.choice(available)
        board[index] = 'O' # AI always plays as 'O'

# Game Setup

def choose_game_mode():
    # Prompts user to select one- or two-player mode.
    while True:
        choice = input("Choose game mode (1 - vs AI, 2 = 2 Players): ")
        if choice in ('1', '2'):
            return choice
        print("Invalid input. Please enter 1 or 2.")

