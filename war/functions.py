"""
Module:
functions.py

This module implements handy functions in the implementations of the
game logic.
"""


# function to create two players
def get_players():
    players = []
    while len(players) < 2:
        user = input("Name of player {}:".format(len(players) + 1))
        players.append(user)
    return players
