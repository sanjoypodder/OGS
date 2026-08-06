"""
===========================================================

OGS Smart Money AI

Liquidity Zone

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ogs.smart_money.swing import Swing


@dataclass(frozen=True, slots=True)
class LiquidityZone:
    """
    Base class for all liquidity zones.
    """

    first_swing: Swing
    second_swing: Swing

    zone_price: Decimal
    tolerance: Decimal

    @property
    def timestamp(self):
        return self.second_swing.timestamp