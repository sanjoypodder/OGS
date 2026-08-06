"""
===========================================================

OGS Smart Money AI

Imbalance Factory

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.imbalance import (
    Imbalance,
    ImbalanceDirection,
)

from .candle_factory import (
    make_bearish_candle,
    make_bullish_candle,
    make_candle,
)


def make_bullish_imbalance() -> Imbalance:

    return Imbalance(
        first=make_bullish_candle(index=0),
        middle=make_bullish_candle(index=1),
        last=make_bullish_candle(index=2),
        direction=ImbalanceDirection.BULLISH,
    )


def make_bearish_imbalance() -> Imbalance:

    return Imbalance(
        first=make_bearish_candle(index=0),
        middle=make_bearish_candle(index=1),
        last=make_bearish_candle(index=2),
        direction=ImbalanceDirection.BEARISH,
    )


def make_bullish_imbalance_candles():

    return [

        make_candle(
            index=0,
            high=100,
            low=90,
            open=95,
            close=98,
        ),

        make_candle(
            index=1,
            high=110,
            low=98,
            open=100,
            close=108,
        ),

        make_candle(
            index=2,
            high=120,
            low=105,
            open=106,
            close=118,
        ),
    ]


def make_bearish_imbalance_candles():

    return [

        make_candle(
            index=0,
            high=110,
            low=100,
            open=108,
            close=102,
        ),

        make_candle(
            index=1,
            high=105,
            low=95,
            open=100,
            close=96,
        ),

        make_candle(
            index=2,
            high=95,
            low=85,
            open=92,
            close=86,
        ),
    ]