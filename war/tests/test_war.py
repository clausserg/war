"""
Unit and regression test for the war package.
"""


import pytest
from unittest import mock
import builtins
from war.functions import get_players
from war.card_class import Card
from war.deck_class import Deck


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
    """Testing the len dunder of the Deck class"""

    my_deck = Deck()
    assert my_deck.__len__() == 52
