# from IPython.display import clear_output
from colorama import Fore
from random import randrange
import time
# Beginning of Function wiring
def draw_board(board,score1,score2):
    print("\n" * 15)
    return Fore.MAGENTA + f"""
                      {board[1]}  |   {board[2]}  |   {board[3]}
                         |      |
                    _____|______|_______
                      {board[4]}  |   {board[5]}  |   {board[6]}
                         |      |
                    _____|______|_______
                      {board[7]}  |   {board[8]}  |   {board[9]}
                         |      |{"Player1 ":>30}: { score1 : <20} {"---":<10} {"Player2 ":<10}: {score2 :<20}
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
def stop_game():
    confirm = not replay()
    if confirm:
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
    return confirm

def space_check(board,position):
    return board[position] == " "
def full_board_check(board):
    for x in range(1,10):
        if space_check(board,x):
            return False
    return True
# End of Function Programs











# Game Play



print("Let's play a game😊")
the_board = ["#"]
the_board.extend([" "] * 10)
player_turn = first_player().lower()
print(f"{player_turn} goes first.")
mark = player1_mark
p1 = 0
p2 = 0
while True:
    try:
        #    Player 1 turn
        if player_turn == "player 1":
            try:
                position = int(input(f"{player_turn} choose a position 1-9 : "))
            except ValueError:
                print("\n" * 15)
                position = int(input(f"Invalid Position ಥ_ಥ\nChoose again : "))
            while (position not in range(1,10) or (the_board[position] != " ")):
                try:
                    position = int(input(f"Invalid Position ಥ_ಥ\nChoose again : "))
                except ValueError:
                    print("\n" * 15)
                    position = int(input(f"Invalid Position ಥ_ಥ\nChoose again : "))
            play(the_board,mark,position)
            print(draw_board(the_board,p1,p2))
            if win_check(the_board,mark):
                print(Fore.BLUE + "Player 1 has won!")
                p1 += 1
                the_board = ["#"]
                the_board.extend([" "] * 10)
                if stop_game():
                    break
            else:
                if full_board_check(the_board):
                    print("Draw!")
                    the_board = ["#"]
                    the_board.extend([" "] * 10)
                    if stop_game():
                        break
                else:
                    player_turn = "player 2"
                    if mark == "O":
                        mark = "X"
                    else:
                        mark = "O"
        #     Player 2 turn
        else:
            if mark == "X":
                mark = "O"
            try:
                position = int(input(f"{player_turn} choose a position 1-9 : "))
            except ValueError:
                print("\n" * 15)
                position = int(input(f"Invalid Position ಥ_ಥ\nChoose again : "))
            while (position not in range(1,10) or (the_board[position] != " ")):
                try:
                    position = int(input(f"Invalid Position ಥ_ಥ\nChoose again : "))
                except ValueError:
                    print("\n" * 15)
                    position = int(input(f"Invalid Position ಥ_ಥ\nChoose again : "))
            play(the_board,mark,position)
            print(draw_board(the_board,p1,p2))
            if win_check(the_board,mark):
                print(Fore.BLUE + "Player 2 has won!")
                p2 += 1
                the_board = ["#"]
                the_board.extend([" "] * 10)
                if stop_game():
                    break
            else:
                if full_board_check(the_board):
                    print("Draw!")
                    the_board = ["#"]
                    the_board.extend([" "] * 10)
                    if stop_game():
                        break
                else:
                    player_turn = "player 2"
                    if mark == "O":
                        mark = "X"
                    else:
                        mark = "O"
            player_turn = "player 1"
            mark = "X"

        #     Player 1 turn
    except KeyboardInterrupt:
        stop_game()
        break
