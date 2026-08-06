"""
Liquidity Void Domain Model
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from ogs.market.candle import Candle

from .enums import LiquidityVoidDirection


@dataclass(slots=True, frozen=True)
class LiquidityVoid:
    """
    Represents an institutional liquidity void.
    """

    first: Candle
    last: Candle

    direction: LiquidityVoidDirection

    top: float
    bottom: float
    midpoint: float
    size: float

    candle_count: int

    is_filled: bool = False
    fill_timestamp: datetime | None = None

    @property
    def is_bullish(self) -> bool:
        return self.direction is LiquidityVoidDirection.BULLISH

    @property
    def is_bearish(self) -> bool:
        return self.direction is LiquidityVoidDirection.BEARISH