"""
===========================================================

OGS Smart Money AI

Market Structure Enums

===========================================================
"""

from enum import Enum


class SwingType(str, Enum):
    """
    Market Structure Swing Types.
    """

    HIGH = "High"

    LOW = "Low"

    HIGHER_HIGH = "Higher High"

    HIGHER_LOW = "Higher Low"

    LOWER_HIGH = "Lower High"

    LOWER_LOW = "Lower Low"


class SwingStrength(str, Enum):
    """
    Swing strength classification.
    """

    WEAK = "Weak"

    NORMAL = "Normal"

    STRONG = "Strong"


class TrendDirection(str, Enum):
    """
    Overall market trend.
    """

    BULLISH = "Bullish"

    BEARISH = "Bearish"

    RANGING = "Ranging"