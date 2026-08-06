"""
OGS Smart Money AI

MarketHoliday Factory
"""

from __future__ import annotations

from datetime import date
from uuid import uuid4

from .domain import MarketHoliday
from .enums import (
    MarketHolidayStatus,
    MarketHolidayType,
)


class MarketHolidayFactory:
    """
    Factory for creating MarketHoliday entities.
    """

    @staticmethod
    def create(
        *,
        name: str,
        holiday_date: date,
        market_holiday_id: str = "",
        exchange: str = "",
        market: str = "",
        country: str = "",
        timezone: str = "UTC",
        holiday_type: MarketHolidayType = (
            MarketHolidayType.UNKNOWN
        ),
        status: MarketHolidayStatus = (
            MarketHolidayStatus.ACTIVE
        ),
        description: str = "",
        active: bool = True,
    ) -> MarketHoliday:
        """
        Create a MarketHoliday instance.
        """

        holiday_id = market_holiday_id.strip()

        if not holiday_id:
            holiday_id = str(uuid4())

        return MarketHoliday(
            market_holiday_id=holiday_id,
            name=name.strip(),
            holiday_date=holiday_date,
            exchange=exchange.strip(),
            market=market.strip(),
            country=country.strip(),
            timezone=timezone.strip() or "UTC",
            holiday_type=holiday_type,
            status=status,
            description=description.strip(),
            active=active,
        )