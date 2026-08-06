"""
===========================================================

OGS Smart Money AI

CorporateEvent Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from .enums import (
    CorporateEventStatus,
    CorporateEventType,
)


@dataclass(slots=True)
class CorporateEvent:
    """
    Corporate event entity.
    """

    corporate_event_id: str = ""

    exchange: str = ""

    market: str = ""

    instrument: str = ""

    event_name: str = ""

    event_date: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    effective_date: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    description: str = ""

    corporate_event_type: CorporateEventType = (
        CorporateEventType.UNKNOWN
    )

    status: CorporateEventStatus = (
        CorporateEventStatus.UNKNOWN
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
            and self.status == CorporateEventStatus.ACTIVE
        )

    @property
    def is_valid(self) -> bool:

        return (
            bool(self.corporate_event_id.strip())
            and bool(self.exchange.strip())
            and bool(self.market.strip())
            and bool(self.instrument.strip())
            and bool(self.event_name.strip())
        )

    def to_dict(self) -> dict:

        return {
            "corporate_event_id": self.corporate_event_id,
            "exchange": self.exchange,
            "market": self.market,
            "instrument": self.instrument,
            "event_name": self.event_name,
            "event_date": self.event_date.isoformat(),
            "effective_date": self.effective_date.isoformat(),
            "description": self.description,
            "corporate_event_type":
                self.corporate_event_type.value,
            "status": self.status.value,
            "active": self.active,
        }

    def __str__(self) -> str:

        return (
            f"CorporateEvent("
            f"id='{self.corporate_event_id}', "
            f"name='{self.event_name}')"
        )