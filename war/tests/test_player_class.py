"""
This is module: test_player_class.py

Unit and regression test for: player_class.py
"""


from war.player_class import Player
from war.deck_class import Deck
import functools


def test_attributes_player():
    """Testing the attributes of a Player object"""

    my_player = Player("Flori")
    assert isinstance(my_player, Player) == True and \
    my_player.name == "Flori" and \
    my_player.cards == []


def test_dunder_player():
    """Testing the dunder methods __len__ and __str__ of a Player object"""

    my_deck = Deck()
    my_deck.shuffle()
    my_player = Player("Flori")
    my_player.get_cards(my_deck.deal_card())
    my_player.get_cards(my_deck.deal_card())
    assert my_player.__str__() == "Flori, has 2 cards!" and \
    my_player.__len__() == 2


def test_getcards_player():
    """Testing the get_cards() method of a Player object"""

    my_deck = Deck()
    my_player = Player("Flori")
    cards = []

    my_player.get_cards(my_deck.deal_card())
    cards.append(my_deck.deal_card())
    cards.append(my_deck.deal_card())
    my_player.get_cards(cards)

    assert len(my_player.cards) == 3 and \
    my_player.cards[0].__str__() == "King of Spades, worth 14 points."


def test_dealcards_player():
    """Testing the deal_cards() method of a Player object"""

    my_deck = Deck()
    my_player = Player("Flori")

    # give some cards to the player
    for idx in range(10):
        my_player.get_cards(my_deck.deal_card())

    cards = []
    cards.append(my_player.deal_cards(at_war=False))
    cards.extend(my_player.deal_cards(at_war=True))
    assert len(cards) == 6
