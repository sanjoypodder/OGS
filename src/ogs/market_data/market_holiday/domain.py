"""
OGS Smart Money AI

MarketHoliday Domain
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, date, datetime

from .enums import (
    MarketHolidayStatus,
    MarketHolidayType,
)


@dataclass(slots=True)
class MarketHoliday:
    """
    Represents a market holiday or special market closure.
    """

    market_holiday_id: str = ""

    name: str = ""

    holiday_date: date | None = None

    exchange: str = ""

    market: str = ""

    country: str = ""

    timezone: str = "UTC"

    holiday_type: MarketHolidayType = (
        MarketHolidayType.UNKNOWN
    )

    status: MarketHolidayStatus = (
        MarketHolidayStatus.UNKNOWN
    )

    description: str = ""

    active: bool = True

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def is_active(self) -> bool:
        """
        Return True when the holiday is active.
        """

        return (
            self.active
            and self.status == MarketHolidayStatus.ACTIVE
        )

    @property
    def is_valid(self) -> bool:
        """
        Return True when the minimum required fields are valid.
        """

        return (
            bool(self.market_holiday_id.strip())
            and bool(self.name.strip())
            and self.holiday_date is not None
        )

    @property
    def is_half_day(self) -> bool:
        """
        Return True for a half-day trading holiday.
        """

        return (
            self.holiday_type
            == MarketHolidayType.HALF_DAY
        )

    @property
    def is_special_trading(self) -> bool:
        """
        Return True for a special trading day.
        """

        return (
            self.holiday_type
            == MarketHolidayType.SPECIAL_TRADING
        )

    @property
    def is_emergency(self) -> bool:
        """
        Return True for an emergency market holiday.
        """

        return (
            self.holiday_type
            == MarketHolidayType.EMERGENCY
        )

    def to_dict(self) -> dict:
        """
        Convert the holiday to a dictionary.
        """

        return {
            "market_holiday_id": self.market_holiday_id,
            "name": self.name,
            "holiday_date": (
                self.holiday_date.isoformat()
                if self.holiday_date is not None
                else None
            ),
            "exchange": self.exchange,
            "market": self.market,
            "country": self.country,
            "timezone": self.timezone,
            "holiday_type": self.holiday_type.value,
            "status": self.status.value,
            "description": self.description,
            "active": self.active,
        }

    def __str__(self) -> str:
        return (
            f"MarketHoliday("
            f"id='{self.market_holiday_id}', "
            f"name='{self.name}', "
            f"date='{self.holiday_date}')"
        )