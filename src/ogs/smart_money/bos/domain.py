"""
===========================================================

OGS Smart Money AI

Break of Structure Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from ogs.market import Candle
from ogs.smart_money.swing import Swing

from .enums import BOSType


@dataclass(frozen=True, slots=True)
class BOS:
    """
    Represents a confirmed Break of Structure.
    """

    candle: Candle
    broken_swing: Swing
    bos_type: BOSType

    @property
    def timestamp(self):
        return self.candle.timestamp

    @property
    def price(self):
        return self.broken_swing.price

    def __str__(self) -> str:
        return (
            f"{self.bos_type.value} "
            f"@ {self.timestamp.isoformat()}"
        )