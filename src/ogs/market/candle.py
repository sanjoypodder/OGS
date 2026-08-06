"""
===========================================================

OGS Smart Money AI

Immutable Candle

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from ogs.market.price import Price
from ogs.market.symbol import Symbol
from ogs.market.timeframe import Timeframe


@dataclass(frozen=True, slots=True)
class Candle:
    """
    Immutable OHLCV candle.
    """

    symbol: Symbol

    timeframe: Timeframe

    timestamp: datetime

    open: Price

    high: Price

    low: Price

    close: Price

    volume: Decimal = Decimal("0")

    def __post_init__(self) -> None:
        """
        Validate OHLC values.
        """

        if self.open.symbol != self.symbol:
            raise ValueError("Open price symbol mismatch.")

        if self.high.symbol != self.symbol:
            raise ValueError("High price symbol mismatch.")

        if self.low.symbol != self.symbol:
            raise ValueError("Low price symbol mismatch.")

        if self.close.symbol != self.symbol:
            raise ValueError("Close price symbol mismatch.")

        if self.high < self.low:
            raise ValueError("High cannot be lower than Low.")

        if self.high < self.open:
            raise ValueError("High cannot be lower than Open.")

        if self.high < self.close:
            raise ValueError("High cannot be lower than Close.")

        if self.low > self.open:
            raise ValueError("Low cannot be higher than Open.")

        if self.low > self.close:
            raise ValueError("Low cannot be higher than Close.")

        if self.volume < 0:
            raise ValueError("Volume cannot be negative.")