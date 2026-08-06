"""
===========================================================

OGS Smart Money AI

Change of Character Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from ogs.market import Candle
from ogs.smart_money.bos import BOS

from .enums import CHOCHType


@dataclass(frozen=True, slots=True)
class CHOCH:
    """
    Represents a confirmed Change of Character.
    """

    candle: Candle
    broken_bos: BOS
    choch_type: CHOCHType

    @property
    def timestamp(self):
        return self.candle.timestamp

    @property
    def price(self):
        return self.broken_bos.price

    def __str__(self) -> str:
        return (
            f"{self.choch_type.value} "
            f"@ {self.timestamp.isoformat()}"
        )