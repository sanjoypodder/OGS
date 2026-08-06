"""
OGS Smart Money AI

MarketHoliday Collection
"""

from __future__ import annotations

from datetime import date

from ogs.smart_money.base.collection import BaseCollection

from .domain import MarketHoliday
from .enums import MarketHolidayType


class MarketHolidayCollection(
    BaseCollection[MarketHoliday],
):
    """
    Collection of MarketHoliday entities.
    """

    @property
    def items(self):
        """
        Return all market holidays.
        """

        return self._items

    def add(
        self,
        holiday: MarketHoliday,
    ) -> None:
        """
        Add a market holiday.
        """

        self._items.append(holiday)

    def find(
        self,
        market_holiday_id: str,
    ) -> MarketHoliday | None:
        """
        Find a holiday by identifier.
        """

        for holiday in self._items:

            if (
                holiday.market_holiday_id
                == market_holiday_id
            ):
                return holiday

        return None

    def find_by_date(
        self,
        holiday_date: date,
    ) -> list[MarketHoliday]:
        """
        Return holidays occurring on a date.
        """

        return [
            holiday
            for holiday in self._items
            if holiday.holiday_date == holiday_date
        ]

    def find_by_exchange(
        self,
        exchange: str,
    ) -> list[MarketHoliday]:
        """
        Return holidays for an exchange.
        """

        normalized_exchange = exchange.strip().upper()

        return [
            holiday
            for holiday in self._items
            if holiday.exchange.strip().upper()
            == normalized_exchange
        ]

    def active(self) -> list[MarketHoliday]:
        """
        Return active holidays.
        """

        return [
            holiday
            for holiday in self._items
            if holiday.is_active
        ]

    def half_days(self) -> list[MarketHoliday]:
        """
        Return half-day holidays.
        """

        return [
            holiday
            for holiday in self._items
            if (
                holiday.holiday_type
                == MarketHolidayType.HALF_DAY
            )
        ]

    def special_trading_days(
        self,
    ) -> list[MarketHoliday]:
        """
        Return special trading days.
        """

        return [
            holiday
            for holiday in self._items
            if (
                holiday.holiday_type
                == MarketHolidayType.SPECIAL_TRADING
            )
        ]

    def emergencies(
        self,
    ) -> list[MarketHoliday]:
        """
        Return emergency holidays.
        """

        return [
            holiday
            for holiday in self._items
            if (
                holiday.holiday_type
                == MarketHolidayType.EMERGENCY
            )
        ]

    def to_list(
        self,
    ) -> list[MarketHoliday]:
        """
        Return holidays as a list.
        """

        return list(self._items)