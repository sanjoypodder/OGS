"""
===========================================================

OGS Smart Money AI

Breaker Block Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from ogs.market.candle import Candle

from .enums import BreakerBlockDirection


@dataclass(slots=True, frozen=True)
class BreakerBlock:
    """
    Represents an ICT Breaker Block.
    """

    candle: Candle

    direction: BreakerBlockDirection

    top: float

    bottom: float

    midpoint: float

    size: float

    is_mitigated: bool = False

    mitigation_timestamp: datetime | None = None

    @property
    def is_bullish(self) -> bool:
        return self.direction is BreakerBlockDirection.BULLISH

    @property
    def is_bearish(self) -> bool:
        return self.direction is BreakerBlockDirection.BEARISH