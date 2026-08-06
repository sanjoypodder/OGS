"""
===========================================================

OGS Smart Money AI

Market Structure Shift Enums

===========================================================
"""

from __future__ import annotations

from enum import StrEnum


class MSSType(StrEnum):
    """
    Market Structure Shift direction.
    """

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"