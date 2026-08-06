"""
===========================================================

OGS Smart Money AI

Change of Character Enums

===========================================================
"""

from __future__ import annotations

from enum import StrEnum


class CHOCHType(StrEnum):
    """
    Change of Character direction.
    """

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"