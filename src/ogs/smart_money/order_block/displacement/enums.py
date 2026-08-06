"""
===========================================================

OGS Smart Money AI

Order Block Displacement Enums

===========================================================
"""

from __future__ import annotations

from enum import StrEnum


class DisplacementDirection(StrEnum):
    """
    Institutional displacement direction.
    """

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"