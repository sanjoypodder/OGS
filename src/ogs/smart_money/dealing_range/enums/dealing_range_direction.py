"""
OGS FinOS

Dealing Range Direction Enum

Author : OGS FinOS
Version : 0.0.2
"""

from enum import Enum


class DealingRangeDirection(str, Enum):
    """
    Institutional dealing range direction.
    """

    BULLISH = "Bullish"

    BEARISH = "Bearish"

    SIDEWAYS = "Sideways"