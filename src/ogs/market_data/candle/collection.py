"""
OGS Smart Money AI
------------------

Market Data - Candle Collection

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from collections.abc import Iterable

from ogs.smart_money.base.collection import BaseCollection

from .domain import Candle
from .enums import CandleDirection


class CandleSeries(
    BaseCollection[Candle],
):
    """
    Collection of Candle objects.
    """

    def __init__(
        self,
        items: Iterable[Candle] | None = None,
    ) -> None:

        super().__init__(items)

    def append(
        self,
        candle: Candle,
    ) -> None:

        self._items.append(candle)

    def latest(
        self,
        count: int = 1,
    ) -> list[Candle]:

        return self._items[-count:]

    def bullish(
        self,
    ) -> list[Candle]:

        return [
            candle
            for candle in self._items
            if candle.direction is CandleDirection.BULLISH
        ]

    def bearish(
        self,
    ) -> list[Candle]:

        return [
            candle
            for candle in self._items
            if candle.direction is CandleDirection.BEARISH
        ]

    def doji(
        self,
    ) -> list[Candle]:

        return [
            candle
            for candle in self._items
            if candle.direction is CandleDirection.DOJI
        ]

    def by_symbol(
        self,
        symbol: str,
    ) -> list[Candle]:

        return [
            candle
            for candle in self._items
            if candle.symbol == symbol
        ]

    def by_timeframe(
        self,
        timeframe: str,
    ) -> list[Candle]:

        return [
            candle
            for candle in self._items
            if candle.timeframe == timeframe
        ]

    def highest_high(self) -> float:

        if not self._items:
            return 0.0

        return max(
            candle.high
            for candle in self._items
        )

    def lowest_low(self) -> float:

        if not self._items:
            return 0.0

        return min(
            candle.low
            for candle in self._items
        )

    def total_volume(self) -> float:

        return sum(
            candle.volume
            for candle in self._items
        )