"""
===========================================================

OGS Smart Money AI

Fair Value Gap Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from ogs.market import Candle

from .enums import FairValueGapDirection


@dataclass(frozen=True, slots=True)
class FairValueGap:
    """
    Represents an institutional Fair Value Gap.
    """

    first: Candle

    middle: Candle

    last: Candle

    direction: FairValueGapDirection

    top: float

    bottom: float

    midpoint: float

    size: float

    is_filled: bool = False

    fill_timestamp: datetime | None = None

    @property
    def is_bullish(self) -> bool:
        """
        Returns True if bullish.
        """
        return (
            self.direction
            is FairValueGapDirection.BULLISH
        )

    @property
    def is_bearish(self) -> bool:
        """
        Returns True if bearish.
        """
        return (
            self.direction
            is FairValueGapDirection.BEARISH
        )