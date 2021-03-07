"""
Unit and regression test for the war package.
"""


import pytest
import mock
import builtins
from war.functions import get_players


def test_get_players_mocking():
    """Testing functions.get_players() using mocking"""

    with mock.patch.object(builtins, 'input', lambda _: 'Flori'):
        assert get_players() == ['Flori', 'Flori']


def test_get_players_monkeypatching(monkeypatch):
    """Testing functions.get_players() using monkeypatching"""

    monkeypatch.setattr('builtins.input', lambda _: "Flori")
    assert get_players() == ['Flori', 'Flori']
