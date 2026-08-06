"""
===========================================================

OGS Smart Money AI

Market Structure Statistics

===========================================================
"""

from __future__ import annotations

from .collection import SwingSeries
from .enums import (
    SwingStrength,
    SwingType,
)


class SwingStatistics:
    """
    Statistics for a SwingSeries.
    """

    def __init__(
        self,
        swings: SwingSeries,
    ) -> None:

        self._swings = swings

    @property
    def count(self) -> int:
        return len(self._swings)

    @property
    def high_count(self) -> int:
        return sum(
            swing.is_high
            for swing in self._swings
        )

    @property
    def low_count(self) -> int:
        return sum(
            swing.is_low
            for swing in self._swings
        )

    @property
    def higher_high_count(self) -> int:
        return sum(
            swing.type is SwingType.HIGHER_HIGH
            for swing in self._swings
        )

    @property
    def higher_low_count(self) -> int:
        return sum(
            swing.type is SwingType.HIGHER_LOW
            for swing in self._swings
        )

    @property
    def lower_high_count(self) -> int:
        return sum(
            swing.type is SwingType.LOWER_HIGH
            for swing in self._swings
        )

    @property
    def lower_low_count(self) -> int:
        return sum(
            swing.type is SwingType.LOWER_LOW
            for swing in self._swings
        )

    @property
    def strong_count(self) -> int:
        return sum(
            swing.strength is SwingStrength.STRONG
            for swing in self._swings
        )

    @property
    def normal_count(self) -> int:
        return sum(
            swing.strength is SwingStrength.NORMAL
            for swing in self._swings
        )

    @property
    def weak_count(self) -> int:
        return sum(
            swing.strength is SwingStrength.WEAK
            for swing in self._swings
        )

    @property
    def latest(self):
        if not self._swings:
            return None

        return self._swings[-1]

    @property
    def oldest(self):
        if not self._swings:
            return None

        return self._swings[0]