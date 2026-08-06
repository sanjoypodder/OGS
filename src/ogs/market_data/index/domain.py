"""
===========================================================

OGS Smart Money AI

Index Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from .enums import (
    IndexStatus,
    IndexType,
)


@dataclass(slots=True)
class Index:
    """
    Market Index.
    """

    index_code: str = ""

    index_name: str = ""

    exchange: str = ""

    market: str = ""

    currency_code: str = ""

    country: str = ""

    index_type: IndexType = (
        IndexType.UNKNOWN
    )

    status: IndexStatus = (
        IndexStatus.UNKNOWN
    )

    base_value: float = 0.0

    current_value: float = 0.0

    constituent_count: int = 0

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
            and self.status == IndexStatus.ACTIVE
        )

    @property
    def is_valid(self) -> bool:

        return (
            bool(self.index_code.strip())
            and bool(self.index_name.strip())
            and bool(self.exchange.strip())
        )

    def to_dict(self) -> dict:

        return {
            "index_code": self.index_code,
            "index_name": self.index_name,
            "exchange": self.exchange,
            "market": self.market,
            "currency_code": self.currency_code,
            "country": self.country,
            "index_type": self.index_type.value,
            "status": self.status.value,
            "base_value": self.base_value,
            "current_value": self.current_value,
            "constituent_count": self.constituent_count,
            "active": self.active,
        }

    def __str__(self) -> str:

        return (
            f"Index("
            f"code='{self.index_code}', "
            f"name='{self.index_name}')"
        )