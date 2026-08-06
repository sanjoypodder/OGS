"""
===========================================================

OGS Smart Money AI

Test Candle Factory

Reusable immutable Candle objects.

===========================================================
"""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal

from ogs.market import (
    Candle,
    Symbol,
    Timeframe,
)

from .price_factory import PriceFactory
from .symbol_factory import SymbolFactory


class CandleFactory:
    """
    Factory for creating immutable Candle objects.

    Every candle created is guaranteed to satisfy:

        High >= Open
        High >= Close
        Low <= Open
        Low <= Close

    so Candle.__post_init__() always succeeds.
    """

    @staticmethod
    def create(
        *,
        symbol: Symbol | None = None,
        timeframe: Timeframe = Timeframe.M1,
        timestamp: datetime | None = None,
        open: int | float | str | Decimal = 100,
        high: int | float | str | Decimal = 105,
        low: int | float | str | Decimal = 95,
        close: int | float | str | Decimal = 102,
        volume: int | float | str | Decimal = 1000,
    ) -> Candle:

        symbol = symbol or SymbolFactory.default()

        timestamp = timestamp or datetime(
            2025,
            1,
            1,
            0,
            0,
            0,
        )

        return Candle(
            symbol=symbol,
            timeframe=timeframe,
            timestamp=timestamp,
            open=PriceFactory.create(symbol, open),
            high=PriceFactory.create(symbol, high),
            low=PriceFactory.create(symbol, low),
            close=PriceFactory.create(symbol, close),
            volume=Decimal(str(volume)),
        )

    # =====================================================
    # Default BTC Candle
    # =====================================================

    @staticmethod
    def btc() -> Candle:

        return CandleFactory.create(
            symbol=SymbolFactory.btc(),
        )

    # =====================================================
    # Gold Candle
    # =====================================================

    @staticmethod
    def gold() -> Candle:

        return CandleFactory.create(
            symbol=SymbolFactory.gold(),
            open=3400,
            high=3415,
            low=3392,
            close=3408,
        )

    # =====================================================
    # EURUSD Candle
    # =====================================================

    @staticmethod
    def eurusd() -> Candle:

        return CandleFactory.create(
            symbol=SymbolFactory.eurusd(),
            open="1.17000",
            high="1.17100",
            low="1.16900",
            close="1.17050",
        )

    # =====================================================
    # Bullish Candle
    # =====================================================

    @staticmethod
    def bullish(
        *,
        symbol: Symbol | None = None,
    ) -> Candle:

        return CandleFactory.create(
            symbol=symbol,
            open=100,
            high=110,
            low=95,
            close=108,
        )

    # =====================================================
    # Bearish Candle
    # =====================================================

    @staticmethod
    def bearish(
        *,
        symbol: Symbol | None = None,
    ) -> Candle:

        return CandleFactory.create(
            symbol=symbol,
            open=110,
            high=112,
            low=98,
            close=100,
        )

    # =====================================================
    # Doji
    # =====================================================

    @staticmethod
    def doji(
        *,
        symbol: Symbol | None = None,
    ) -> Candle:

        return CandleFactory.create(
            symbol=symbol,
            open=100,
            high=103,
            low=97,
            close=100,
        )

    # =====================================================
    # Custom Timestamp
    # =====================================================

    @staticmethod
    def at(
        timestamp: datetime,
        *,
        symbol: Symbol | None = None,
    ) -> Candle:

        return CandleFactory.create(
            symbol=symbol,
            timestamp=timestamp,
        )

    # =====================================================
    # Sequence
    # =====================================================

    @staticmethod
    def sequence(
        count: int = 10,
        *,
        symbol: Symbol | None = None,
        timeframe: Timeframe = Timeframe.M1,
    ) -> list[Candle]:

        symbol = symbol or SymbolFactory.default()

        candles = []

        start = datetime(2025, 1, 1)

        for i in range(count):

            candles.append(

                CandleFactory.create(

                    symbol=symbol,

                    timeframe=timeframe,

                    timestamp=start.replace(
                        minute=i,
                    ),

                    open=100 + i,

                    high=105 + i,

                    low=95 + i,

                    close=102 + i,

                    volume=1000 + i,

                )

            )

        return candles