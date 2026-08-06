"""
===========================================================

OGS Smart Money AI

Break of Structure Enums

===========================================================
"""

from __future__ import annotations

from enum import StrEnum


class BOSType(StrEnum):
    """
    Break of Structure direction.
    """

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"