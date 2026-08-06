"""
===========================================================

OGS Smart Money AI

Liquidity Sweep Enums

===========================================================
"""

from __future__ import annotations

from enum import StrEnum


class SweepDirection(StrEnum):
    """
    Sweep direction.
    """

    BUY_SIDE = "BUY_SIDE"
    SELL_SIDE = "SELL_SIDE"


class SweepStatus(StrEnum):
    """
    Sweep confirmation status.
    """

    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"