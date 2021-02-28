"""
Module:
war.py

War card game written for fun while following the
'Complete Python Developer Certification Course' by Imtiaz Ahmad, on Udemy.
This is the main module of the War cards game, contains the game logic.
"""

from card_class import Card
from deck_class import Deck
from player_class import Player
from table_class import Table
from functions import get_players
import random


if __name__ == "__main__":

    # get player names
    player_names = get_players()
    playing = True  # players are playing

    # start the actual War game
    while playing:
        # create Deck object and shuffle it
        deck = Deck()
        deck.shuffle()

        # randomize which player is created first and goes first in game
        # then create Player objects
        random.shuffle(player_names)
        player_one = Player(player_names[0])
        player_two = Player(player_names[1])

        # deal cards to players from the deck
        while len(deck):  # i.e. is not empty
            player_one.get_cards(deck.deal_card())
            player_two.get_cards(deck.deal_card())

        # create the gaming table
        table = Table(player_one.name, player_two.name)

        # game session miscellaneous
        round = 0  # counting the rounds

        # game session starts here
        while True:
            round += 1
            print("This is round {}!". format(round))
            at_war = False  # players are not at war by default
            # check win conditions
            if len(player_one) == 0:
                print(player_one)
                print("{} lost the game!".format(player_one.name))
                break
            elif len(player_two) == 0:
                print(player_two)
                print("{} lost the game!".format(player_two.name))
                break
            else:
                # each player drops a card on the table
                table.get_cards(player_one.name, player_one.deal_cards(1))
                table.get_cards(player_two.name, player_two.deal_cards(1))

                # show the table
                print('\n')
                print(table)

                # player collects the cards if his card down has higher value
                if table.winning() == player_one.name:
                    player_one.get_cards(table.return_cards())
                elif table.winning() == player_two.name:
                    player_two.get_cards(table.return_cards())
                else:  # means players are at war, enter at_war loop
                    print(table.winning())
                    at_war = True
                    while at_war:
                        if len(player_one) < 5:
                            print("Not enough cards!")
                            at_war = False
                            break
                        elif len(player_two) < 5:
                            print("Not enough cards!")
                            at_war = False
                            break
                        else:
                            table.get_cards(player_one.name, player_one.deal_cards(10))
                            table.get_cards(player_two.name, player_two.deal_cards(10))
                            print(table)
                            if table.winning() == player_one.name:
                                print("{} won this WAR wound!".format(player_one.name))
                                player_one.get_cards(table.return_cards())
                                at_war = False
                                break
                            elif table.winning() == player_two.name:
                                print("{} won this WAR wound!".format(player_two.name))
                                player_two.get_cards(table.return_cards())
                                at_war = False
                                break
                            else:
                                print(table.winning())
                                continue
        playing = False
