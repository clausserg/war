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
