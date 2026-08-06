"""
===========================================================

OGS Smart Money AI

Order Block Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from ogs.market import Candle

from ogs.smart_money.mss import MSS
from ogs.smart_money.liquidity.sweep import (
    LiquiditySweep,
)

from .enums import (
    OrderBlockDirection,
    OrderBlockStatus,
)


@dataclass(frozen=True, slots=True)
class OrderBlock:
    """
    Institutional Order Block.
    """

    origin_candle: Candle

    mss: MSS

    liquidity_sweep: LiquiditySweep

    direction: OrderBlockDirection

    status: OrderBlockStatus

    @property
    def timestamp(self):

        return self.origin_candle.timestamp

    @property
    def high(self):

        return self.origin_candle.high

    @property
    def low(self):

        return self.origin_candle.low

    @property
    def open(self):

        return self.origin_candle.open

    @property
    def close(self):

        return self.origin_candle.close

    def __str__(self):

        return (
            f"{self.direction.value} "
            f"Order Block @ "
            f"{self.timestamp.isoformat()}"
        )