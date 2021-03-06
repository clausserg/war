"""
Module:
functions.py

Implements handy functions for the game logic.
1. get_players() function: set up player names.
"""


# function to create two players
def get_players():
    """
    This function returns a list of two player names.

    :return: list of two strings
    """

    players = []
    while len(players) < 2:
        #  let's get appropriate names, w/o spaces or special characters!
        while True:
            user = input("Name of player {}:".format(len(players) + 1))
            if user.isalnum():
                players.append(user)
                break
            else:
                print("Sorry, player name cannot contain a space or special characters.")
                print("Please insert an appropriate name, e.g. 'John'!")
    return players
