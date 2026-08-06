"""
OGS Smart Money AI
------------------

Market Data - Candle Enums

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from enum import Enum


class CandleDirection(str, Enum):
    """
    Candle direction.
    """

    BULLISH = "Bullish"
    BEARISH = "Bearish"
    DOJI = "Doji"


class PriceType(str, Enum):
    """
    Price type.
    """

    OPEN = "Open"
    HIGH = "High"
    LOW = "Low"
    CLOSE = "Close"
    MEDIAN = "Median"
    TYPICAL = "Typical"
    WEIGHTED = "Weighted"


class CandleSource(str, Enum):
    """
    Candle source.
    """

    LIVE = "Live"
    HISTORICAL = "Historical"
    SIMULATED = "Simulated"
    BACKTEST = "Backtest"


class CandleStatus(str, Enum):
    """
    Candle lifecycle status.
    """

    FORMING = "Forming"
    CLOSED = "Closed"


class VolumeType(str, Enum):
    """
    Volume classification.
    """

    REAL = "Real"
    TICK = "Tick"
    UNKNOWN = "Unknown"