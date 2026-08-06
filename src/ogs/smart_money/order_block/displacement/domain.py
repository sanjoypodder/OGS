"""
===========================================================

OGS Smart Money AI

Order Block Displacement Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from ogs.market import Candle

from .enums import DisplacementDirection


@dataclass(
    frozen=True,
    slots=True,
)
class Displacement:
    """
    Represents institutional displacement
    following an Order Block.
    """

    candle: Candle

    direction: DisplacementDirection

    @property
    def timestamp(self):
        return self.candle.timestamp

    @property
    def high(self):
        return self.candle.high

    @property
    def low(self):
        return self.candle.low

    @property
    def open(self):
        return self.candle.open

    @property
    def close(self):
        return self.candle.close

    def __str__(self):

        return (
            f"{self.direction.value} "
            f"Displacement @ "
            f"{self.timestamp.isoformat()}"
        )