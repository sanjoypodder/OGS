"""
===========================================================

OGS Smart Money AI

Imbalance Enums

===========================================================
"""

from __future__ import annotations

from enum import Enum, auto


class ImbalanceDirection(Enum):
    """
    Direction of an imbalance.
    """

    BULLISH = auto()
    BEARISH = auto()