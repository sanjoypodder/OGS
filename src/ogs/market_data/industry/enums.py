"""
OGS Smart Money AI

Industry Enums
"""

from __future__ import annotations

from enum import Enum


class IndustryType(Enum):
    """
    Industry classification.
    """

    UNKNOWN = "UNKNOWN"

    MANUFACTURING = "MANUFACTURING"

    SERVICES = "SERVICES"

    FINANCIAL = "FINANCIAL"

    TECHNOLOGY = "TECHNOLOGY"

    HEALTHCARE = "HEALTHCARE"

    ENERGY = "ENERGY"

    CUSTOM = "CUSTOM"


class IndustryStatus(Enum):
    """
    Industry status.
    """

    UNKNOWN = "UNKNOWN"

    ACTIVE = "ACTIVE"

    INACTIVE = "INACTIVE"

    DELISTED = "DELISTED"