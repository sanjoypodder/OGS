"""
===========================================================

OGS Smart Money AI

Equal Low Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from ogs.smart_money.liquidity.base import LiquidityZone

from .enums import EqualLowType


@dataclass(frozen=True, slots=True)
class EqualLow(LiquidityZone):
    """
    Represents an Equal Low liquidity zone.
    """

    equal_low_type: EqualLowType

    def __str__(self) -> str:

        return (
            f"{self.equal_low_type.value} "
            f"Equal Low @ {self.zone_price}"
        )