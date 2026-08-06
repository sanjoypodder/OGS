"""
===========================================================

OGS Smart Money AI

Order Block Enums

===========================================================
"""

from __future__ import annotations

from enum import StrEnum


class OrderBlockDirection(StrEnum):
    BULLISH = "BULLISH"
    BEARISH = "BEARISH"


class OrderBlockStatus(StrEnum):
    ACTIVE = "ACTIVE"
    MITIGATED = "MITIGATED"
    INVALIDATED = "INVALIDATED"