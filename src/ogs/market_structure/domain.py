"""
===========================================================

OGS Smart Money AI

Market Structure Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from ogs.market import Candle

from .enums import (
    SwingStrength,
    SwingType,
)


@dataclass(
    frozen=True,
    slots=True,
)
class SwingPoint:
    """
    Represents a market structure swing.
    """

    symbol: str

    candle: Candle

    index: int

    price: float

    type: SwingType

    strength: SwingStrength = SwingStrength.NORMAL

    @property
    def timestamp(self):
        """
        Swing timestamp.
        """
        return self.candle.timestamp

    @property
    def is_high(self) -> bool:
        return self.type in (
            SwingType.HIGH,
            SwingType.HIGHER_HIGH,
            SwingType.LOWER_HIGH,
        )

    @property
    def is_low(self) -> bool:
        return self.type in (
            SwingType.LOW,
            SwingType.HIGHER_LOW,
            SwingType.LOWER_LOW,
        )

    @property
    def is_higher_high(self) -> bool:
        return self.type is SwingType.HIGHER_HIGH

    @property
    def is_higher_low(self) -> bool:
        return self.type is SwingType.HIGHER_LOW

    @property
    def is_lower_high(self) -> bool:
        return self.type is SwingType.LOWER_HIGH

    @property
    def is_lower_low(self) -> bool:
        return self.type is SwingType.LOWER_LOW

    @property
    def is_strong(self) -> bool:
        return self.strength is SwingStrength.STRONG

    @property
    def is_weak(self) -> bool:
        return self.strength is SwingStrength.WEAK