"""
===========================================================

OGS Smart Money AI

Market Structure Shift Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from ogs.market import Candle
from ogs.smart_money.choch import CHOCH

from .enums import MSSType


@dataclass(frozen=True, slots=True)
class MSS:
    """
    Represents a confirmed Market Structure Shift.
    """

    candle: Candle
    triggering_choch: CHOCH
    mss_type: MSSType

    @property
    def timestamp(self):
        return self.candle.timestamp

    @property
    def price(self):
        return self.triggering_choch.price

    def __str__(self) -> str:
        return (
            f"{self.mss_type.value} "
            f"@ {self.timestamp.isoformat()}"
        )