"""
===========================================================

OGS Smart Money AI

Rejection Block Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from ogs.market.candle import Candle

from .enums import RejectionBlockDirection


@dataclass(slots=True, frozen=True)
class RejectionBlock:
    """
    Represents an ICT Rejection Block.
    """

    candle: Candle

    direction: RejectionBlockDirection

    top: float

    bottom: float

    midpoint: float

    size: float

    is_confirmed: bool = False

    confirmation_timestamp: datetime | None = None

    @property
    def is_bullish(self) -> bool:
        return self.direction is RejectionBlockDirection.BULLISH

    @property
    def is_bearish(self) -> bool:
        return self.direction is RejectionBlockDirection.BEARISH