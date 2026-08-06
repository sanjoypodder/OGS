"""
===========================================================

OGS Smart Money AI

Candle Series

===========================================================
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass

from ogs.market.candle import Candle


@dataclass(slots=True)
class CandleSeries:
    """
    Collection of candles.

    This class becomes the input for every future market engine.
    """

    candles: list[Candle]

    def __len__(self) -> int:
        return len(self.candles)

    def __iter__(self) -> Iterator[Candle]:
        return iter(self.candles)

    def __getitem__(self, index: int) -> Candle:
        return self.candles[index]

    @property
    def first(self) -> Candle:
        return self.candles[0]

    @property
    def last(self) -> Candle:
        return self.candles[-1]

    def previous(self) -> Candle:
        if len(self.candles) < 2:
            raise IndexError("Series contains fewer than two candles.")
        return self.candles[-2]

    def latest(self, count: int) -> "CandleSeries":
        return CandleSeries(self.candles[-count:])

    def window(self, start: int, end: int) -> "CandleSeries":
        return CandleSeries(self.candles[start:end])

    def append(self, candle: Candle) -> None:
        self.candles.append(candle)

    @property
    def is_empty(self) -> bool:
        return len(self.candles) == 0