# Name : Mohamed Safaa AbdelGawad
# The Game Number : 7 -> subtract square game .
# Algorithm of game :
# 1- enter number of coins for play
# 2-get input from player one
# 3-check if the number has a square root or not if it has the game will continue if not put the correct number
# 4-check if the square number if it is bigger than coins put a square number less than coins if it less continue
# the game
# 5-after check from (3-4)/ subtract a square number from number of coins
# 6- check if the result of subtraction (number of coins ) = 0 if it true the game will stop and player one is win
# if it not ,continues the game with reminder of coins
# 7-get input from player two
# 8- repeat the steps (3-4-5) with player two
# 9- check if the result of subtraction (number of coins ) = 0 if it true the game will stop and player two is win
# if it not ,continues the game with reminder of coins
# 10- the game will stop when anyone from two player remove the last coin

import math

global play

print(
    "welcome to subtract a square:) \ngame mode ... \nalways removing a non-zero square number of coins\nthe player "
    "who removes the last coin wins "
    "\n\nENJOY")


while True:
    n_coins = input("number of coins you want to play ")  # GET NUMBER OF COINS

    if n_coins.isdigit():  # If move is a number
        n_coins = int(n_coins)
        break

    else:
        print("Invalid input\nTry Again \n")


# this function show to the players the number of the remaining coins in the game to allow to them choose the
# square number you want to subtract.
def display_state():
    global n_coins
    print("Remaining coins = ", n_coins)


# Get number of coins the player wants to play
# noinspection PyGlobalUndefined
def get_input(player):
    global move
    valid = False

    while not valid:  # Repeat until a valid move is entered
        message = player + " player  enter square  coins  "
        move = input(message)  # Get move as string

        if move.isdigit():  # If move is a number
            move = int(move)

            root = math.sqrt(move)  # get square root
            if int(root + 0.5) ** 2 == move:  # check the number is prefect square or not
                if play == 0:  #
                    if move < n_coins:  # defence condition to make sure user take INPUT less than
                        # num coins and bigger than zero
                        valid = True

                    if not valid:
                        print("Invalid input\nTry Again \n")

                else:
                    if move <= n_coins:  # defence condition after first turn to make sure user take  CORRECT INPUT
                        valid = True

                    if not valid:
                        print("Invalid input\nTry Again \n")
            else:
                print("Invalid input\nTry Again \n")
        else:
            print("Invalid input\nTry Again \n")

    return move


# Update number of coins after taking some coins
def update_state(coins_taken):
    global n_coins
    n_coins -= coins_taken


# Check if he is taking the last coin and wins
def is_winner():
    global n_coins
    if n_coins < 1:
        return True


def play_subtract_square_game():  # FUNCTION FOR CHANGE BETWEEN TWO PLAYER
    global play
    play = 0
    while True:
        first = get_input("First")
        update_state(first)  # RETURN FUNCTION TO UPDATE NUMBER OF COINS
        display_state()  # RETURN FUNCTION TO RETURN REMAINING COINS
        play += 1

        if is_winner():
            print("first player won")
            break
        second = get_input("Second")
        update_state(second)
        display_state()
        play += 1
        if is_winner():
            print("second player won")
            break


play_subtract_square_game()
