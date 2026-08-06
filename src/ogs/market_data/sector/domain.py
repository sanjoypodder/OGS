"""
===========================================================

OGS Smart Money AI

Sector Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from .enums import (
    SectorStatus,
    SectorType,
)


@dataclass(slots=True)
class Sector:
    """
    Market Sector.
    """

    sector_code: str = ""

    sector_name: str = ""

    market: str = ""

    country: str = ""

    description: str = ""

    parent_sector: str = ""

    sector_type: SectorType = (
        SectorType.UNKNOWN
    )

    status: SectorStatus = (
        SectorStatus.UNKNOWN
    )

    active: bool = True

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def is_active(self) -> bool:

        return (
            self.active
            and self.status == SectorStatus.ACTIVE
        )

    @property
    def is_valid(self) -> bool:

        return (
            bool(self.sector_code.strip())
            and bool(self.sector_name.strip())
        )

    def to_dict(self) -> dict:

        return {
            "sector_code": self.sector_code,
            "sector_name": self.sector_name,
            "market": self.market,
            "country": self.country,
            "description": self.description,
            "parent_sector": self.parent_sector,
            "sector_type": self.sector_type.value,
            "status": self.status.value,
            "active": self.active,
        }

    def __str__(self) -> str:

        return (
            f"Sector("
            f"code='{self.sector_code}', "
            f"name='{self.sector_name}')"
        )