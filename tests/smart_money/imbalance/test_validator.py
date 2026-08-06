"""
===========================================================

OGS Smart Money AI

Imbalance Validator Tests

===========================================================
"""

from ogs.smart_money.imbalance import (
    Imbalance,
    ImbalanceDirection,
    ImbalanceValidator,
)

from tests.factories import (
    make_bullish_candle,
)


def make_imbalance():

    return Imbalance(
        first=make_bullish_candle(),
        middle=make_bullish_candle(),
        last=make_bullish_candle(),
        direction=ImbalanceDirection.BULLISH,
    )


def test_valid():

    validator = ImbalanceValidator()

    assert validator.validate(
        make_imbalance()
    )


def test_none():

    validator = ImbalanceValidator()

    assert not validator.validate(None)