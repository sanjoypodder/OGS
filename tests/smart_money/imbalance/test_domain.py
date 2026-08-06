"""
===========================================================

OGS Smart Money AI

Imbalance Domain Tests

===========================================================
"""

from ogs.smart_money.imbalance import (
    Imbalance,
    ImbalanceDirection,
)

from tests.factories import (
    make_bullish_candle,
    make_bearish_candle,
)


def test_create_bullish():

    imbalance = Imbalance(
        first=make_bullish_candle(),
        middle=make_bullish_candle(),
        last=make_bullish_candle(),
        direction=ImbalanceDirection.BULLISH,
    )

    assert imbalance.is_bullish
    assert not imbalance.is_bearish


def test_create_bearish():

    imbalance = Imbalance(
        first=make_bearish_candle(),
        middle=make_bearish_candle(),
        last=make_bearish_candle(),
        direction=ImbalanceDirection.BEARISH,
    )

    assert imbalance.is_bearish
    assert not imbalance.is_bullish


def test_first_exists():

    imbalance = Imbalance(
        first=make_bullish_candle(),
        middle=make_bullish_candle(),
        last=make_bullish_candle(),
        direction=ImbalanceDirection.BULLISH,
    )

    assert imbalance.first is not None


def test_middle_exists():

    imbalance = Imbalance(
        first=make_bullish_candle(),
        middle=make_bullish_candle(),
        last=make_bullish_candle(),
        direction=ImbalanceDirection.BULLISH,
    )

    assert imbalance.middle is not None


def test_last_exists():

    imbalance = Imbalance(
        first=make_bullish_candle(),
        middle=make_bullish_candle(),
        last=make_bullish_candle(),
        direction=ImbalanceDirection.BULLISH,
    )

    assert imbalance.last is not None