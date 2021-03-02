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
    game_over = False  # players start playing

    # start the actual War game
    while not game_over:
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
        round = 0  # counting the rounds

        # game session starts here
        playing = True
        while playing:
            round += 1
            print("This is round {}!". format(round))
            at_war = False  # players are not at war by default

            # check win conditions
            if not len(player_one):
                print(player_one)
                print("{} lost the game!".format(player_one.name))
                playing = False
                break
            elif not len(player_two):
                print(player_two)
                print("{} lost the game!".format(player_two.name))
                playing = False
                break
            else:
                pass # go on with the game

            # each player drops a card on the table
            table.get_cards(player_one.name, player_one.deal_cards(at_war))
            table.get_cards(player_two.name, player_two.deal_cards(at_war))

            # show the table
            print('\n')
            print(table)

            # player collects the cards if his card down has higher value
            if table.winning() == player_one.name:
                player_one.get_cards(table.return_cards())
            elif table.winning() == player_two.name:
                player_two.get_cards(table.return_cards())
            else:  # means players are at war, enter at_war loop
                at_war = True
                print(table.winning())
                #  check if players can start the war session
                if len(player_one) < 10:
                    print("But {} has less than 10 cards!".format(player_one.name))
                    print("{} lost the game!".format(player_one.name))
                    playing = False
                    break
                elif len(player_two) < 10:
                    print("But {} has less than 10 cards!".format(player_two.name))
                    print("{} lost the game!".format(player_two.name))
                    playing = False
                    break

            # deal with players at war
            while at_war:
                # players drop 10 cards on the table
                table.get_cards(player_one.name, player_one.deal_cards(at_war))
                table.get_cards(player_two.name, player_two.deal_cards(at_war))
                # show the table again
                print(table)

                # check who has the highest card value down on the table
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
                    print(table.winning() + " AGAIN!")
                    # check is war session can continue or somebody lost the game
                    if len(player_one) < 10:
                        print("But {} has less than 10 cards!".format(player_one.name))
                        print("{} lost the game!".format(player_one.name))
                        playing = False
                        break
                    elif len(player_two) < 10:
                        print("But {} has less than 10 cards!".format(player_two.name))
                        print("{} lost the game!".format(player_two.name))
                        playing = False
                        break

        # ask players if they play again
        while True:
            game_on = input("Go for another game (yes/no)?")
            if len(game_on) and game_on[0].lower() == 'y':
                game_over = False
                break
            elif not len(game_on) or game_on[0] == 'n':
                game_over = True
                break
            else:
                print("Didn't get that. Please say 'yes' or 'no'!")
