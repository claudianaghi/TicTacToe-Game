# board
# display
# play game
# check win check rows, columns, diagonals
# check tie board full
# flip player


# ----GLobal variables-----


# Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

# If game is still going
game_still_going = True

# Who won? Or tie?
winner = None


#Whos turn is it?
current_player = "X"


# display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# play game of tictactoe
def play_game():
    display_board() #diplay initial board

    # while the game is still going
    while game_still_going:

        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # flip to the other player
        flip_player()

     # The game has ended
    if winner == "X" or winner == "0":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# handle a single turn of an arbitrary player
def handle_turn(player):

    print(player + " 's turn. ")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("I Choose a position fron 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
             valid = True
        else:
             print("You cant go there. Go again.")

    board[position] = player

    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    # set up global variables
    global winner

    #check rows
    row_winner = check_rows()

    #check columns
    column_winner = check_columns()

    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        #there is a win
        winner = row_winner

    elif column_winner:
        #there is a win
        winner = column_winner


    elif diagonal_winner:
        # there is a win
        winner = diagonal_winner


    else:
        #there is no win
        winner = None

    return


def check_rows():
    # set up global ariables
    global game_still_going
    #check if the rows all have the same value and not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False


    # return the winner X or O
    if row_1:
        return board[0]

    elif row_2:
        return board[3]

    elif row_3:
        return board[6]

    return

def check_columns():
    # set up global ariables
    global game_still_going
    # check if the rows all have the same value and not empty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    # return the winner X or O
    if column_1:
        return board[0]

    elif column_2:
        return board[1]

    elif column_3:
        return board[2]
    return

def check_diagonals():
    # set up global ariables
    global game_still_going
    # check if the rows all have the same value and not empty

    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"


    if diagonals_1 or diagonals_2:
        game_still_going = False

    # return the winner X or O
    if diagonals_1:
        return board[0]

    elif diagonals_2:
        return board[6]

    return


def check_if_tie():

    global game_still_going

    if "-" not in board:
        game_still_going = False

    return

def flip_player():

    global current_player

    if current_player == "X":
        current_player = "0"

    elif current_player == "0":
        current_player = "X"

    return



play_game()



