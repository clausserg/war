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
    game_over = False

    # start the actual War game
    while not game_over:
        # create a new deck of cards and shuffle it
        deck = Deck()
        deck.shuffle()

        # randomize which player goes first in game
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
            # deal with infinite loops
            if round > 10000:
                print(f"{player_one.name} and {player_two.name} are in infinite loop!")
                print(f"{player_one.name} and {player_two.name} are shuffling their cards!")
                # shuffle player cards
                player_one.shuffle()
                player_two.shuffle()
                # reset round counter
                round = 0

            # check win/lose conditions
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
                print("New game session starts here!")
                pass # go on with the game

            # each player drops a card on the table
            table.get_cards(player_one.name, player_one.deal_cards(at_war=False))
            table.get_cards(player_two.name, player_two.deal_cards(at_war=False))

            # assume that players are at war by default after first round
            at_war = True

            # deal with players at war
            while at_war:
                print(table)  # show the gaming table
                # check win conditions or if at war
                if table.winning() == player_one.name:
                    player_one.get_cards(table.return_cards())
                    at_war = False
                elif table.winning() == player_two.name:
                    player_two.get_cards(table.return_cards())
                    at_war = False
                else:  # players are at war
                # check if war can be declared, i.e. palyers have more than 5 cards
                    if len(player_one) < 5:
                        print("{} has less than 5 cards!".format(player_one.name))
                        print("{} lost the game!".format(player_one.name))
                        playing = False  # end game session
                        break  # end current at_war loop
                    elif len(player_two) < 5:
                        print("{} has less than 5 cards!".format(player_two.name))
                        print("{} lost the game!".format(player_two.name))
                        playing = False  # end game session
                        break  # end current at_war loop
                    else:
                        print("At War!!!")
                        # players drop 5 cards on the table
                        table.get_cards(player_one.name, player_one.deal_cards(at_war=True))
                        table.get_cards(player_two.name, player_two.deal_cards(at_war=True))

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
