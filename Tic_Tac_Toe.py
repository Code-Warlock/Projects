# from IPython.display import clear_output
# from colorama import Fore
from random import randrange
import time
def draw_board(board):
    # clear_output()
    print("\n" * 20)
    return f"""
                      {board[1]}  |   {board[2]}  |   {board[3]}
                         |      |
                    _____|______|_______
                      {board[4]}  |   {board[5]}  |   {board[6]}
                         |      |
                    _____|______|_______
                      {board[7]}  |   {board[8]}  |   {board[9]}
                         |      |
    """
def flip_coin():
    turn = randrange(2)
    if turn == 0:
        return "X","O"
    return "O","X"
def marker_select():
    marker1 = flip_coin()[0]
    return marker1
player1_mark = ""
def first_player():
    player1 = input("Player1 choose a marker : ").upper()
    while player1 not in ("X","O"):
        player1 = input("Player1 choose a marker : ").upper()
    global player1_mark
    player1_mark = player1
    if player1_mark != flip_coin()[0]:
        return "Player 2"
    return "Player 1"
def play(board,mark,position):
    board[position] = mark
def win_check(board,mark):
    return board[1] == board[2] == board[3] == mark or board[4] == board[5] == board[6] == mark or board[7] == board[8] == board[9] == mark or board[1] == board[5]== board[9] == mark or board[3] == board[5]== board[7] == mark or board[1] == board[4]== board[7] == mark or board[2] == board[5]== board[8] == mark or board[3] == board[6]== board[9] == mark
def replay():
    ans = input("Do you want to continue? : ").lower()
    return ans in ("yeah","y","ya","","yes")
print("Let's play a game😊")
the_board = ["#"]
the_board.extend([" "] * 10)
player_turn = first_player().lower()
print(f"{player_turn} goes first.")
mark = player1_mark
while True:
#     Player 1 turn

    if player_turn == "player 1":
        position = int(input(f"{player_turn} choose a position 1-9 : "))
        while (position not in range(1,10) or (the_board[position] != " ")):
            position = int(input(f"Invalid Position ಥ_ಥ\nChoose again : "))
        play(the_board,mark,position)
        print(draw_board(the_board))
        if win_check(the_board,mark):
            print("Player 1 has won!")
            the_board = ["#"]
            the_board.extend([" "] * 10)
            if not replay():
                print("Closing Program" , end="")
                time.sleep(0.5)
                print(".",end="")
                time.sleep(0.5)
                print(".",end="")
                time.sleep(0.5)
                print(".",end="")
                time.sleep(0.4)
                print("\b",end="")
                time.sleep(0.4)
                print("\b",end="")
                time.sleep(0.4)
                print("\b",end="")
                time.sleep(0.4)
                print(".",end="")
                time.sleep(0.4)
                print(".",end="")
                time.sleep(0.4)
                print(".",end="\n")
                time.sleep(0.4)
                print("Game Over")
                break
        player_turn = "player 2"
        if mark == "O":
            mark = "X"
        else:
            mark = "O"
#     Player 2 turn
    else:
        if mark == "X":
            mark = "O"
        position = int(input(f"{player_turn} choose a position 1-9 : "))
        while (position not in range(1,10) or (the_board[position] != " ")):
            position = int(input(f"Invalid Position ಥ_ಥ\nChoose again : "))
        play(the_board,mark,position)
        print(draw_board(the_board))

        if win_check(the_board,mark):
            print("Player 2 has won!")
            the_board = ["#"]
            the_board.extend([" "] * 10)
            if not replay():
                print("Closing Program", end="")
                time.sleep(0.5)
                print(".",end="")
                time.sleep(0.5)
                print(".",end="")
                time.sleep(0.5)
                print(".",end="")
                time.sleep(0.4)
                print("\b",end="")
                time.sleep(0.4)
                print("\b",end="")
                time.sleep(0.4)
                print("\b",end="")
                time.sleep(0.4)
                print(".",end="")
                time.sleep(0.4)
                print(".",end="")
                time.sleep(0.4)
                print(".",end="\n")
                time.sleep(0.4)
                print("Game Over")
                break
        player_turn = "player 1"
        mark = "X"
