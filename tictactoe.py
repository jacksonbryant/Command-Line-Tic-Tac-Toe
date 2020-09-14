import sys

# Global variables
p1_name = ""
p2_name = ""
p1_XorO_choice = ""
p2_XorO_choice = ""
p1_score = 0
p2_score = 0
draw_count = 0
round_num = 1
four_spaces = "    "


# Initializes the game
def game_start():
    print("------------------------------------------------------------------------------------------------------------------------")
    print("    Welcome to Command-Line Tic-Tac-Toe!".upper())
    print("")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("    Enter S to start the game.")
    print("    Enter Q to quit.")

    start_or_quit = input("    ")

    if start_or_quit == "S" or start_or_quit == "s":
        print("")
        get_names()
        Xs_or_Os()
        game_continue_menu()

    elif start_or_quit == "Q" or start_or_quit == "q":
        print("")
        print("   Goodbye!")
        sys.exit()

    else:
        print("")
        print("    ERROR: Please enter S or Q.")
        print("")
        game_start()


# Gets the user-inputted player names
def get_names():
    global p1_name
    global p2_name

    print("    Player 1, what is your name?")
    p1_name = input("    ")
    print("    Hello, " + p1_name)
    print("    ")
    print("    Player 2, what is your name?")
    p2_name = input("    ")
    print("    Hello, " + p2_name)

# Allows Player 1 to choose if he/she wants to be Xs or Os


def Xs_or_Os():

    global p1_XorO_choice
    global p2_XorO_choice

    print("")
    print("    " + p1_name +
          ", do you want to be Xs or Os? (Enter X or O)")
    p1_XorO_choice = input("    ")

    if p1_XorO_choice == "X" or p1_XorO_choice == "x":
        print("")
        print("    " + p1_name + ", you are Xs")
        print("    " + p2_name + ", you are Os.")
        p1_XorO_choice = "X"
        p2_XorO_choice = "O"

    elif p1_XorO_choice == "O" or p1_XorO_choice == "o":
        print("")
        print("    " + p1_name + ", you are Os")
        print("    " + p2_name + ", you are Xs.")
        p2_XorO_choice = "X"
        p1_XorO_choice = "O"

    elif p1_XorO_choice != "X" and p1_XorO_choice != "x" and p1_XorO_choice != "O" and p1_XorO_choice != "o":
        print("")
        print("    ERROR: Please enter X or O!")
        Xs_or_Os()

# Asks players if he/she wants to proceed with the game or quit after entering their names and choosing between Xs and Os


def game_continue_menu():
    print('')
    print("    Press C to continue. \n    Press Q to quit.")
    cont_choice = input("    ")

    if cont_choice == "C" or cont_choice == "c":
        print("")
        game_play()
    elif cont_choice == "Q" or cont_choice == "q":
        print("")
        print("    Goodbye!")
        sys.exit()
    else:
        print("    ERROR: Please enter C or Q!")
        game_continue_menu()

# Gameplay logic


def game_play():

    board = "    0 1 2\n    3 4 5\n    6 7 8"
    p1_wins = False
    p2_wins = False
    p1_choice = ""
    p2_choice = ""
    global p1_score
    global p2_score
    global draw_count
    global round_num

    # Keep playing while there are open spaces on the board
    while "0" in board or "1" in board or "2" in board or "3" in board or "4" in board or "5" in board or "6" in board or "7" in board or "8" in board or p1_choice != "Q" or p1_choice != "q" or p2_choice != "Q" or p2_choice != "q":

        print("")
        print("------------------------------------------------------------------------------------------------------------------------")
        print("    ROUND " + str(round_num))
        print("")
        print("------------------------------------------------------------------------------------------------------------------------")
        print(board)
        print("")
        print("    " + p1_name + ", choose a number 0-9 to insert an " +
              p1_XorO_choice.upper() + " and make your move.")
        print("")
        print("    Enter R to restart.")
        print("    Enter Q to quit.")
        p1_choice = input("    ")

        # Error handling for invalid entry
        while p1_choice != "0" and p1_choice != "1" and p1_choice != "2" and p1_choice != "3" and p1_choice != "4" and p1_choice != "5" and p1_choice != "6" and p1_choice != "7" and p1_choice != "8" and p1_choice != "R" and p1_choice != "r" and p1_choice != "Q" and p1_choice != "q":
            print("")
            print("    ERROR: Invalid entry!")
            print("")
            print(board)
            print("")
            print("    " + p1_name + ", choose a number 0-9 to insert an " +
                  p1_XorO_choice.upper() + " and make your move.")
            print("")
            p1_choice = input("    ")

        # Break loop if user quits
        if p1_choice == "Q" or p1_choice == "q":
            break

         # Restarts current game
        if p1_choice == "R" or p1_choice == "r":
            break

        board = board.replace(p1_choice, p1_XorO_choice)

        # Logic for determining winning sequences
        if p1_XorO_choice == "X":
            if board[4] == "X" and board[14] == "X" and board[24] == "X":
                p1_wins = True
                break
            elif board[6] == "X" and board[16] == "X" and board[26] == "X":
                p1_wins = True
                break
            elif board[8] == "X" and board[18] == "X" and board[28] == "X":
                p1_wins = True
                break
            elif board[4] == "X" and board[6] == "X" and board[8] == "X":
                p1_wins = True
                break
            if board[14] == "X" and board[16] == "X" and board[18] == "X":
                p1_wins = True
                break
            elif board[24] == "X" and board[26] == "X" and board[28] == "X":
                p1_wins = True
                break
            elif board[4] == "X" and board[16] == "X" and board[28] == "X":
                p1_wins = True
                break
            elif board[8] == "X" and board[16] == "X" and board[24] == "X":
                p1_wins = True
                break
        elif p1_XorO_choice == "O":
            if board[4] == "O" and board[14] == "O" and board[24] == "O":
                p1_wins = True
                break
            elif board[6] == "O" and board[16] == "O" and board[26] == "O":
                p1_wins = True
                break
            elif board[8] == "O" and board[18] == "O" and board[28] == "O":
                p1_wins = True
                break
            elif board[4] == "O" and board[6] == "O" and board[8] == "O":
                p1_wins = True
                break
            if board[14] == "O" and board[16] == "O" and board[18] == "O":
                p1_wins = True
                break
            elif board[24] == "O" and board[26] == "O" and board[28] == "O":
                p1_wins = True
                break
            elif board[4] == "O" and board[16] == "O" and board[28] == "O":
                p1_wins = True
                break
            elif board[8] == "O" and board[16] == "O" and board[24] == "O":
                p1_wins = True
                break
            print("")
        print("------------------------------------------------------------------------------------------------------------------------")
        print("    ROUND " + str(round_num))
        print("")
        print("------------------------------------------------------------------------------------------------------------------------")
        print(board)
        print("")

        # End game if all spaces are occupied (game is drawn)
        if "0" not in board and "1" not in board and "2" not in board and "3" not in board and "4" not in board and "5" not in board and "6" not in board and "7" not in board and "8" not in board:
            break
        print("    " + p2_name + ", choose a number 0-9 to insert an " +
              p2_XorO_choice.upper() + " and make your move.")
        print("")
        print("    Enter R to restart.")
        print("    Enter Q to Quit.")
        p2_choice = input("    ")
        while p2_choice != "0" and p2_choice != "1" and p2_choice != "2" and p2_choice != "3" and p2_choice != "4" and p2_choice != "5" and p2_choice != "6" and p2_choice != "7" and p2_choice != "8" and p2_choice != "Q" and p2_choice != "q" and p2_choice != "R" and p2_choice != "r":
            print("    ERROR: Invalid entry!")
            print("")
            print(board)
            print("")
            print("    " + p2_name + ", choose a number 0-9 to insert an " +
                  p2_XorO_choice.upper() + " and make your move.")
            print("")
            p2_choice = input("    ")
        if p2_choice == "Q" or p2_choice == "q":
            break
        elif p2_choice == "R" or p2_choice == "r":
            break

        board = board.replace(p2_choice, p2_XorO_choice)

        # Logic for determining winning sequences
        if p2_XorO_choice == "X":
            if board[4] == "X" and board[14] == "X" and board[24] == "X":
                p2_wins = True
                break
            elif board[6] == "X" and board[16] == "X" and board[26] == "X":
                p2_wins = True
                break
            elif board[8] == "X" and board[18] == "X" and board[28] == "X":
                p2_wins = True
                break
            elif board[4] == "X" and board[6] == "X" and board[8] == "X":
                p2_wins = True
                break
            if board[14] == "X" and board[16] == "X" and board[18] == "X":
                p2_wins = True
                break
            elif board[24] == "X" and board[26] == "X" and board[28] == "X":
                p2_wins = True
                break
            elif board[4] == "X" and board[16] == "X" and board[28] == "X":
                p2_wins = True
                break
            elif board[8] == "X" and board[16] == "X" and board[24] == "X":
                p2_wins = True
                break
        elif p2_XorO_choice == "O":
            if board[4] == "O" and board[14] == "O" and board[24] == "O":
                p2_wins = True
                break
            elif board[6] == "O" and board[16] == "O" and board[26] == "O":
                p2_wins = True
                break
            elif board[8] == "O" and board[18] == "O" and board[28] == "O":
                p2_wins = True
                break
            elif board[4] == "O" and board[6] == "O" and board[8] == "O":
                p2_wins = True
                break
            if board[14] == "O" and board[16] == "O" and board[18] == "O":
                p2_wins = True
                break
            elif board[24] == "O" and board[26] == "O" and board[28] == "O":
                p2_wins = True
                break
            elif board[4] == "O" and board[16] == "O" and board[28] == "O":
                p2_wins = True
                break
            elif board[8] == "O" and board[16] == "O" and board[24] == "O":
                p2_wins = True
                break
        print("")

        if p2_choice == "Q" or p1_choice == "q":
            break
    # Console output if game is a draw
    if "0" not in board and "1" not in board and "2" not in board and "3" not in board and "4" not in board and "5" not in board and "6" not in board and "7" not in board and "8" not in board:
        draw_count += 1
        print("")
        print(board)
        print("------------------------------------------------------------------------------------------------------------------------")
        print("    CAT got it!")
        print("")
        print("    Score:")
        print("    " + p1_name + ": " + str(p1_score))
        print("    " + p2_name + ": " + str(p2_score))
        print("    Drawn: " + str(draw_count))
        print("")
        print("------------------------------------------------------------------------------------------------------------------------")
        print("")
        print("    Enter P to play again.")
        print("    Enter C to edit names.")
        print("    Enter Q to quit.")
        print("    ")
        play_again = input("    ")
        while play_again != "P" and play_again != "p" and play_again != "C" and play_again != "c" and play_again != "Q" and play_again != "q":
            print("")
            print("    ERROR: Invalid entry!")
            print("")
            print("    Enter P to play again.")
            print("    Enter C to change players and reset score.")
            print("    Enter Q to quit.")
            play_again = input("    ")
        print("")
        if play_again == "P" or play_again == "p":
            game_play()
        elif play_again == "C" or play_again == "c":
            print("")
            get_names()
            game_continue_menu()
        elif play_again == "Q" or play_again == "q":
            print("")

    # Console output if Player 1 wins
    elif p1_wins == True:
        p1_score += 1
        print("")
        print(board)
        print("------------------------------------------------------------------------------------------------------------------------")
        print("    " + p1_name + " wins!")
        print("")
        print("    Score:")
        print("    " + p1_name + ": " + str(p1_score))
        print("    " + p2_name + ": " + str(p2_score))
        print("    Drawn: " + str(draw_count))
        print("")
        print("------------------------------------------------------------------------------------------------------------------------")
        print("    Enter P to play again.")
        print("    Enter C to change players and reset score.")
        print("    Enter Q to quit.")
        print("    ")
        play_again = input("    ")
        while play_again != "P" and play_again != "p" and play_again != "C" and play_again != "c" and play_again != "Q" and play_again != "q":
            print("")
            print("    ERROR: Invalid entry!")
            print("")
            print("    Enter P to play again.")
            print("    Enter C to change players and reset score.")
            print("    Enter Q to quit.")
            play_again = input("    ")
        if play_again == "P" or play_again == "p":
            round_num += 1
            game_play()
        elif play_again == "C" or play_again == "c":
            p1_score = 0
            p2_score = 0
            get_names()
            game_continue_menu()
        elif play_again == "Q" or play_again == "q":
            print("")

    # Console output if Player 2 wins
    elif p2_wins == True:
        p2_score += 1
        print("")
        print(board)
        print("------------------------------------------------------------------------------------------------------------------------")
        print("    " + p2_name + " wins!")
        print("")
        print("    Score:")
        print("    " + p1_name + ": " + str(p1_score))
        print("    " + p2_name + ": " + str(p2_score))
        print("    Drawn: " + str(draw_count))
        print("")
        print("------------------------------------------------------------------------------------------------------------------------")
        print("    Press P to play again.")
        print("    Press C to change players and reset score.")
        print("    Press Q to quit.")
        print("    ")
        play_again = input("    ")
        while play_again != "P" and play_again != "p" and play_again != "C" and play_again != "c" and play_again != "Q" and play_again != "q":
            print("")
            print("    ERROR: Invalid entry!")
            print("")
            print("    Enter P to play again.")
            print("    Enter C to change players and reset score.")
            print("    Enter Q to quit.")
            play_again = input("    ")
        print("")
        if play_again == "P" or play_again == "p":
            game_play()
        elif play_again == "C" or play_again == "c":
            p1_score = 0
            p2_score = 0
            get_names()
            game_continue_menu()
        elif play_again == "Q" or play_again == "q":
            print("")

    # User breaks first while loop by resterting or quitting the game.
    if p1_choice == "R" or p1_choice == "r" or p2_choice == "R" or p2_choice == "r":
        print("")
        print("    Game restarted!")
        print("")
        round_num = 1
        game_play()
    else:
        print("")
        print("    Goodbye!")
        sys.exit()


# Method call that begins the game
game_start()
