"""
===========================================================

OGS Smart Money AI

Mitigation Block Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from ogs.market.candle import Candle

from .enums import MitigationBlockDirection


@dataclass(slots=True, frozen=True)
class MitigationBlock:
    """
    Represents an ICT Mitigation Block.
    """

    candle: Candle

    direction: MitigationBlockDirection

    top: float

    bottom: float

    midpoint: float

    size: float

    is_mitigated: bool = False

    mitigation_timestamp: datetime | None = None

    @property
    def is_bullish(self) -> bool:
        return self.direction is MitigationBlockDirection.BULLISH

    @property
    def is_bearish(self) -> bool:
        return self.direction is MitigationBlockDirection.BEARISH