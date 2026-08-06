"""
===========================================================

OGS Smart Money AI

Swing Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from ogs.market import Candle

from .enums import SwingType


@dataclass(frozen=True, slots=True)
class Swing:
    """
    Represents a confirmed market swing.
    """

    index: int
    candle: Candle
    swing_type: SwingType

    @property
    def timestamp(self):
        return self.candle.timestamp

    @property
    def price(self):
        if self.swing_type == SwingType.HIGH:
            return self.candle.high
        return self.candle.low

    def __str__(self) -> str:
        return (
            f"{self.swing_type.value} "
            f"@ {self.timestamp.isoformat()}"
        )