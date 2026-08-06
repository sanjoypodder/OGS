"""
===========================================================

OGS Smart Money AI

Industry Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from .enums import (
    IndustryStatus,
    IndustryType,
)


@dataclass(slots=True)
class Industry:
    """
    Market Industry.
    """

    industry_code: str = ""

    industry_name: str = ""

    sector_code: str = ""

    market: str = ""

    country: str = ""

    description: str = ""

    industry_type: IndustryType = (
        IndustryType.UNKNOWN
    )

    status: IndustryStatus = (
        IndustryStatus.UNKNOWN
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
            and self.status == IndustryStatus.ACTIVE
        )

    @property
    def is_valid(self) -> bool:

        return (
            bool(self.industry_code.strip())
            and bool(self.industry_name.strip())
            and bool(self.sector_code.strip())
        )

    def to_dict(self) -> dict:

        return {
            "industry_code": self.industry_code,
            "industry_name": self.industry_name,
            "sector_code": self.sector_code,
            "market": self.market,
            "country": self.country,
            "description": self.description,
            "industry_type": self.industry_type.value,
            "status": self.status.value,
            "active": self.active,
        }

    def __str__(self) -> str:

        return (
            f"Industry("
            f"code='{self.industry_code}', "
            f"name='{self.industry_name}')"
        )