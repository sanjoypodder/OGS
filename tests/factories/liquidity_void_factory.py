"""
Liquidity Void Factory
"""

from ogs.market.candle import Candle
from ogs.smart_money.liquidity_void import (
    LiquidityVoid,
    LiquidityVoidDirection,
)

from .candle_factory import make_candle


def make_bullish_liquidity_void() -> LiquidityVoid:
    first = make_candle(
        open=100,
        high=105,
        low=95,
        close=100,
    )

    last = make_candle(
        open=112,
        high=118,
        low=110,
        close=116,
    )

    return LiquidityVoid(
        first=first,
        last=last,
        direction=LiquidityVoidDirection.BULLISH,
        top=110,
        bottom=105,
        midpoint=107.5,
        size=5,
        candle_count=3,
    )


def make_bearish_liquidity_void() -> LiquidityVoid:
    first = make_candle(
        open=100,
        high=105,
        low=95,
        close=100,
    )

    last = make_candle(
        open=88,
        high=90,
        low=84,
        close=85,
    )

    return LiquidityVoid(
        first=first,
        last=last,
        direction=LiquidityVoidDirection.BEARISH,
        top=95,
        bottom=90,
        midpoint=92.5,
        size=5,
        candle_count=3,
    )


def make_bullish_liquidity_void_candles() -> list[Candle]:
    return [
        make_candle(
            open=100,
            high=105,
            low=95,
            close=101,
        ),
        make_candle(
            open=103,
            high=108,
            low=102,
            close=107,
        ),
        make_candle(
            open=112,
            high=118,
            low=110,
            close=116,
        ),
    ]


def make_bearish_liquidity_void_candles() -> list[Candle]:
    return [
        make_candle(
            open=100,
            high=105,
            low=95,
            close=100,
        ),
        make_candle(
            open=96,
            high=98,
            low=92,
            close=93,
        ),
        make_candle(
            open=88,
            high=90,
            low=84,
            close=85,
        ),
    ]