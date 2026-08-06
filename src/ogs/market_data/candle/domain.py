"""
OGS Smart Money AI
------------------

Market Data - Candle Domain

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .enums import (
    CandleDirection,
    CandleSource,
    CandleStatus,
    VolumeType,
)


@dataclass(frozen=True, slots=True)
class Candle:
    """
    Immutable OHLCV candle.
    """

    symbol: str
    timeframe: str

    timestamp: datetime

    open: float
    high: float
    low: float
    close: float

    volume: float = 0.0

    source: CandleSource = CandleSource.HISTORICAL
    status: CandleStatus = CandleStatus.CLOSED
    volume_type: VolumeType = VolumeType.UNKNOWN

    @property
    def direction(self) -> CandleDirection:

        if self.close > self.open:
            return CandleDirection.BULLISH

        if self.close < self.open:
            return CandleDirection.BEARISH

        return CandleDirection.DOJI

    @property
    def body_size(self) -> float:

        return abs(self.close - self.open)

    @property
    def range(self) -> float:

        return self.high - self.low

    @property
    def upper_wick(self) -> float:

        return self.high - max(
            self.open,
            self.close,
        )

    @property
    def lower_wick(self) -> float:

        return min(
            self.open,
            self.close,
        ) - self.low

    @property
    def midpoint(self) -> float:

        return (self.high + self.low) / 2

    @property
    def typical_price(self) -> float:

        return (
            self.high
            + self.low
            + self.close
        ) / 3

    @property
    def weighted_price(self) -> float:

        return (
            self.high
            + self.low
            + (2 * self.close)
        ) / 4

    @property
    def is_bullish(self) -> bool:

        return self.direction is CandleDirection.BULLISH

    @property
    def is_bearish(self) -> bool:

        return self.direction is CandleDirection.BEARISH

    @property
    def is_doji(self) -> bool:

        return self.direction is CandleDirection.DOJI