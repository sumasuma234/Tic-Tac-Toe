import random

board = [" " for i in range(9)]

def print_board():
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print()

def check_win(player):
    win_cond = [(0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6)]
    for a,b,c in win_cond:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw():
    return " " not in board

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("That spot is already taken.")
        except (IndexError, ValueError):
            print("Invalid input! Enter a number between 1 and 9.")

def computer_move():
    print("Computer's turn...")
    empty_indices = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty_indices)
    board[move] = "O"

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X'. Computer is 'O'.")
    print_board()

    while True:
        player_move()
        print_board()
        if check_win("X"):
            print("You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        computer_move()
        print_board()
        if check_win("O"):
            print("Computer wins!")
            break
        if is_draw():
            print("It's a draw!")
            break

play_game()
