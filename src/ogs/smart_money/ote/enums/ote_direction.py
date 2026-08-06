"""
OGS FinOS

OTE Direction

Author : OGS FinOS
Version : 0.0.2
"""

from enum import Enum


class OTEDirection(str, Enum):
    """
    Institutional OTE direction.
    """

    BULLISH = "Bullish"

    BEARISH = "Bearish"