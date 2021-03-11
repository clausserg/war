"""
Unit and regression test for the war package.
"""


import pytest
from unittest import mock
import builtins
from war.functions import get_players
from war.card_class import Card
from war.deck_class import Deck
from war.player_class import Player


def test_get_players_mocking():
    """Testing functions.get_players() using mocking"""

    with mock.patch.object(builtins, 'input', lambda _: 'Flori'):
        assert get_players() == ['Flori', 'Flori']


def test_get_players_monkeypatching(monkeypatch):
    """Testing functions.get_players() using monkeypatching"""

    monkeypatch.setattr('builtins.input', lambda _: "Flori")
    assert get_players() == ['Flori', 'Flori']


def test_card_class():
    """Testing the print dunder of a Card object"""

    my_card = Card("Clubs", "Three", 3)
    assert my_card.__str__() == "Three of Clubs, worth 3 points."


def test_len_deck_class():
    """Testing the dimension of a Deck object"""

    my_deck_one = Deck()
    my_deck_two = Deck()
    my_deck_one.shuffle()
    my_deck_two.shuffle()
    assert my_deck_one.__len__() == 52 and my_deck_two.__len__() == 52


def test_player_class():
    """Testing the Player class"""
    my_deck = Deck()
    my_deck.shuffle()
    my_player = Player("Flori")
    assert my_player.name == "Flori"
    my_player.get_cards(my_deck.deal_card())
    my_player.get_cards(my_deck.deal_card())
    assert my_player.__str__() == "Flori, has 2 cards!" and \
            my_player.__len__() == 2
    my_player.deal_cards()
    assert my_player.__len__() == 1
