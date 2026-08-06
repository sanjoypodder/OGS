"""
===========================================================

OGS Smart Money AI

Liquidity Sweep Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from ogs.market import Candle
from ogs.smart_money.liquidity.buy_side import (
    BuySideLiquidity,
)
from ogs.smart_money.liquidity.sell_side import (
    SellSideLiquidity,
)

from .enums import (
    SweepDirection,
    SweepStatus,
)


@dataclass(frozen=True, slots=True)
class LiquiditySweep:
    """
    Represents a confirmed liquidity sweep.
    """

    liquidity_pool: (
        BuySideLiquidity
        | SellSideLiquidity
    )

    sweep_candle: Candle

    direction: SweepDirection

    status: SweepStatus

    @property
    def timestamp(self):

        return self.sweep_candle.timestamp

    @property
    def sweep_price(self):

        return self.sweep_candle.high

    def __str__(self):

        return (
            f"{self.direction.value} "
            f"Sweep @ {self.timestamp.isoformat()}"
        )