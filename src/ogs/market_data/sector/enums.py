"""
OGS Smart Money AI

Sector Enums
"""

from __future__ import annotations

from enum import Enum


class SectorType(Enum):
    """
    Sector classification.
    """

    UNKNOWN = "UNKNOWN"

    PRIMARY = "PRIMARY"

    SECONDARY = "SECONDARY"

    TERTIARY = "TERTIARY"

    THEMATIC = "THEMATIC"

    CUSTOM = "CUSTOM"


class SectorStatus(Enum):
    """
    Sector status.
    """

    UNKNOWN = "UNKNOWN"

    ACTIVE = "ACTIVE"

    INACTIVE = "INACTIVE"

    DELISTED = "DELISTED"