"""
===========================================================

OGS Smart Money AI

Screener Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from .enums import (
    ScreenerStatus,
    ScreenerType,
)


@dataclass(slots=True)
class Screener:
    """
    Market Screener.
    """

    screener_id: str = ""

    screener_name: str = ""

    description: str = ""

    market: str = ""

    owner: str = ""

    filters: list[dict] = field(
        default_factory=list
    )

    sort_by: str = ""

    sort_order: str = "ASC"

    screener_type: ScreenerType = (
        ScreenerType.UNKNOWN
    )

    status: ScreenerStatus = (
        ScreenerStatus.UNKNOWN
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
            and self.status == ScreenerStatus.ACTIVE
        )

    @property
    def is_valid(self) -> bool:

        return (
            bool(self.screener_id.strip())
            and bool(self.screener_name.strip())
        )

    @property
    def filter_count(self) -> int:

        return len(self.filters)

    def add_filter(
        self,
        filter_rule: dict,
    ) -> None:

        self.filters.append(filter_rule)

    def remove_filter(
        self,
        filter_rule: dict,
    ) -> None:

        if filter_rule in self.filters:
            self.filters.remove(filter_rule)

    def to_dict(self) -> dict:

        return {
            "screener_id": self.screener_id,
            "screener_name": self.screener_name,
            "description": self.description,
            "market": self.market,
            "owner": self.owner,
            "filters": list(self.filters),
            "sort_by": self.sort_by,
            "sort_order": self.sort_order,
            "screener_type": self.screener_type.value,
            "status": self.status.value,
            "active": self.active,
        }

    def __str__(self) -> str:

        return (
            f"Screener("
            f"id='{self.screener_id}', "
            f"name='{self.screener_name}')"
        )