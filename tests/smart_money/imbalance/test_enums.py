"""
===========================================================

OGS Smart Money AI

Imbalance Enum Tests

===========================================================
"""

from ogs.smart_money.imbalance import ImbalanceDirection


def test_bullish_exists():

    assert ImbalanceDirection.BULLISH.name == "BULLISH"


def test_bearish_exists():

    assert ImbalanceDirection.BEARISH.name == "BEARISH"


def test_two_members():

    assert len(ImbalanceDirection) == 2


def test_members_are_unique():

    assert (
        ImbalanceDirection.BULLISH
        != ImbalanceDirection.BEARISH
    )