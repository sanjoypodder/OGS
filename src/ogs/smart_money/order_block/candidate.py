"""
===========================================================

OGS Smart Money AI

Order Block Candidate

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from ogs.market import Candle

from ogs.smart_money.candidate import (
    BaseCandidate,
)

from ogs.smart_money.mss import MSS
from ogs.smart_money.liquidity.sweep import (
    LiquiditySweep,
)


@dataclass(frozen=True, slots=True)
class OrderBlockCandidate(
    BaseCandidate,
):
    """
    Candidate Order Block before validation.
    """

    origin_candle: Candle

    mss: MSS

    liquidity_sweep: LiquiditySweep

    @property
    def timestamp(self):

        return self.origin_candle.timestamp

    def __str__(self):

        return (
            "Order Block Candidate @ "
            f"{self.timestamp.isoformat()}"
        )   