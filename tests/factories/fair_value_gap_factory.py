"""
===========================================================

OGS Smart Money AI

Fair Value Gap Factory

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.fair_value_gap import (
    FairValueGap,
    FairValueGapDirection,
)

from .candle_factory import (
    make_bullish_candle,
    make_bearish_candle,
)


def make_bullish_fair_value_gap() -> FairValueGap:

    return FairValueGap(
        first=make_bullish_candle(index=0),
        middle=make_bullish_candle(index=1),
        last=make_bullish_candle(index=2),
        direction=FairValueGapDirection.BULLISH,
        top=120,
        bottom=100,
        midpoint=110,
        size=20,
    )


def make_bearish_fair_value_gap() -> FairValueGap:

    return FairValueGap(
        first=make_bearish_candle(index=0),
        middle=make_bearish_candle(index=1),
        last=make_bearish_candle(index=2),
        direction=FairValueGapDirection.BEARISH,
        top=120,
        bottom=100,
        midpoint=110,
        size=20,
    )

from .candle_factory import make_candle


def make_bullish_fvg_candles():

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
            high=108,
            low=96,
            open=98,
            close=105,
        ),

        make_candle(
            index=2,
            high=120,
            low=105,
            open=106,
            close=118,
        ),
    ]


def make_bearish_fvg_candles():

    return [

        make_candle(
            index=0,
            high=110,
            low=100,
            open=108,
            close=104,
        ),

        make_candle(
            index=1,
            high=104,
            low=96,
            open=100,
            close=97,
        ),

        make_candle(
            index=2,
            high=95,
            low=85,
            open=92,
            close=88,
        ),
    ]