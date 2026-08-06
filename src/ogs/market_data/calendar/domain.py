"""
===========================================================

OGS Smart Money AI

Calendar Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, date, datetime

from .enums import (
    CalendarStatus,
    CalendarType,
)


@dataclass(slots=True)
class Calendar:
    """
    Trading Calendar.
    """

    calendar_id: str = ""

    exchange: str = ""

    market: str = ""

    trading_date: date | None = None

    calendar_type: CalendarType = CalendarType.UNKNOWN

    status: CalendarStatus = CalendarStatus.CLOSED

    description: str = ""

    active: bool = True

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def is_trading_day(self) -> bool:

        return (
            self.calendar_type == CalendarType.TRADING_DAY
            and self.status == CalendarStatus.OPEN
        )

    @property
    def is_valid(self) -> bool:

        return (
            bool(self.calendar_id.strip())
            and bool(self.exchange.strip())
            and bool(self.market.strip())
            and self.trading_date is not None
        )

    def to_dict(self) -> dict:

        return {
            "calendar_id": self.calendar_id,
            "exchange": self.exchange,
            "market": self.market,
            "trading_date": self.trading_date,
            "calendar_type": self.calendar_type.value,
            "status": self.status.value,
            "description": self.description,
            "active": self.active,
        }

    def __str__(self) -> str:

        return (
            f"Calendar("
            f"id='{self.calendar_id}', "
            f"date='{self.trading_date}')"
        )