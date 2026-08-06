"""
OGS Smart Money AI

MarketHoliday Factory
"""

from __future__ import annotations

from copy import deepcopy
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

    The factory provides:

    - generic MarketHoliday creation
    - typed convenience constructors
    - safe cloning of existing holiday entities

    Domain validation remains the responsibility of the
    MarketHoliday validation layer.
    """

    @staticmethod
    def create(
        *,
        name: str = "",
        holiday_date: date | None = None,
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

    @classmethod
    def _typed(
        cls,
        holiday_type: MarketHolidayType,
        **kwargs,
    ) -> MarketHoliday:
        """
        Create a holiday with a predefined holiday type.
        """

        kwargs["holiday_type"] = holiday_type

        return cls.create(**kwargs)

    @classmethod
    def national(cls, **kwargs) -> MarketHoliday:
        """Create a national holiday."""

        return cls._typed(
            MarketHolidayType.NATIONAL,
            **kwargs,
        )

    @classmethod
    def exchange(cls, **kwargs) -> MarketHoliday:
        """Create an exchange holiday."""

        return cls._typed(
            MarketHolidayType.EXCHANGE,
            **kwargs,
        )

    @classmethod
    def bank(cls, **kwargs) -> MarketHoliday:
        """Create a bank holiday."""

        return cls._typed(
            MarketHolidayType.BANK,
            **kwargs,
        )

    @classmethod
    def religious(cls, **kwargs) -> MarketHoliday:
        """Create a religious holiday."""

        return cls._typed(
            MarketHolidayType.RELIGIOUS,
            **kwargs,
        )

    @classmethod
    def public(cls, **kwargs) -> MarketHoliday:
        """Create a public holiday."""

        return cls._typed(
            MarketHolidayType.PUBLIC,
            **kwargs,
        )

    @classmethod
    def special_trading(
        cls,
        **kwargs,
    ) -> MarketHoliday:
        """Create a special-trading holiday."""

        return cls._typed(
            MarketHolidayType.SPECIAL_TRADING,
            **kwargs,
        )

    @classmethod
    def half_day(cls, **kwargs) -> MarketHoliday:
        """Create a half-day holiday."""

        return cls._typed(
            MarketHolidayType.HALF_DAY,
            **kwargs,
        )

    @classmethod
    def emergency(cls, **kwargs) -> MarketHoliday:
        """Create an emergency holiday."""

        return cls._typed(
            MarketHolidayType.EMERGENCY,
            **kwargs,
        )

    @classmethod
    def custom(cls, **kwargs) -> MarketHoliday:
        """Create a custom holiday."""

        return cls._typed(
            MarketHolidayType.CUSTOM,
            **kwargs,
        )

    @staticmethod
    def clone(
        holiday: MarketHoliday,
    ) -> MarketHoliday:
        """
        Create an independent copy of a MarketHoliday.
        """

        if not isinstance(holiday, MarketHoliday):
            raise TypeError(
                "holiday must be a MarketHoliday instance"
            )

        return deepcopy(holiday)