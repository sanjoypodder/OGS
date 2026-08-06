"""
===========================================================

OGS Smart Money AI

Equal High Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from ogs.smart_money.liquidity.base import LiquidityZone

from .enums import EqualHighType


@dataclass(frozen=True, slots=True)
class EqualHigh(LiquidityZone):
    """
    Represents an Equal High liquidity zone.
    """

    equal_high_type: EqualHighType

    def __str__(self) -> str:

        return (
            f"{self.equal_high_type.value} "
            f"Equal High @ {self.zone_price}"
        )