"""
OGS Smart Money AI
------------------

Market Data - Timeframe Enums

Author : Om Ganapati Solution
Version: 1.0.0
"""

from __future__ import annotations

from enum import Enum


class TimeframeType(str, Enum):
    """
    Standard trading timeframes.
    """

    M1 = "M1"
    M5 = "M5"
    M15 = "M15"
    M30 = "M30"

    H1 = "H1"
    H4 = "H4"

    D1 = "D1"

    W1 = "W1"

    MN1 = "MN1"