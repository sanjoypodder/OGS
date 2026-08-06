"""
OGS Smart Money AI
------------------

Market Data - Candle Factory

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from datetime import datetime

from .domain import Candle
from .enums import (
    CandleSource,
    CandleStatus,
    VolumeType,
)
from .validator import CandleValidator


class CandleFactory:
    """
    Factory for creating validated Candle objects.
    """

    _validator = CandleValidator()

    @classmethod
    def create(
        cls,
        symbol: str,
        timeframe: str,
        timestamp: datetime,
        open: float,
        high: float,
        low: float,
        close: float,
        volume: float = 0.0,
        source: CandleSource = CandleSource.HISTORICAL,
        status: CandleStatus = CandleStatus.CLOSED,
        volume_type: VolumeType = VolumeType.UNKNOWN,
    ) -> Candle:

        candle = Candle(
            symbol=symbol,
            timeframe=timeframe,
            timestamp=timestamp,
            open=open,
            high=high,
            low=low,
            close=close,
            volume=volume,
            source=source,
            status=status,
            volume_type=volume_type,
        )

        if not cls._validator.validate(candle):
            raise ValueError("Invalid Candle.")

        return candle