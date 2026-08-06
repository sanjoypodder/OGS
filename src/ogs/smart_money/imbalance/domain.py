"""
===========================================================

OGS Smart Money AI

Imbalance Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from ogs.market import Candle

from .enums import ImbalanceDirection


@dataclass(frozen=True)
class Imbalance:
    """
    Represents a generic market imbalance.
    """

    first: Candle
    middle: Candle
    last: Candle

    direction: ImbalanceDirection

    @property
    def is_bullish(self) -> bool:
        return self.direction is ImbalanceDirection.BULLISH

    @property
    def is_bearish(self) -> bool:
        return self.direction is ImbalanceDirection.BEARISH