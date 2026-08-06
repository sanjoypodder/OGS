"""
OGS Smart Money AI

MarketHoliday Statistics
"""

from __future__ import annotations

from .collection import MarketHolidayCollection
from .enums import (
    MarketHolidayStatus,
    MarketHolidayType,
)


class MarketHolidayStatistics:
    """
    Statistics for MarketHoliday collections.
    """

    @staticmethod
    def summary(
        holidays: MarketHolidayCollection,
    ) -> dict:
        """
        Return summary statistics.
        """

        items = holidays.to_list()

        return {
            "count": len(items),
            "active": sum(
                1
                for holiday in items
                if holiday.is_active
            ),
            "half_day": sum(
                1
                for holiday in items
                if holiday.holiday_type
                == MarketHolidayType.HALF_DAY
            ),
            "special_trading": sum(
                1
                for holiday in items
                if holiday.holiday_type
                == MarketHolidayType.SPECIAL_TRADING
            ),
            "emergency": sum(
                1
                for holiday in items
                if holiday.holiday_type
                == MarketHolidayType.EMERGENCY
            ),
        }

    @staticmethod
    def type_distribution(
        holidays: MarketHolidayCollection,
    ) -> dict[str, int]:
        """
        Return distribution by holiday type.
        """

        items = holidays.to_list()

        return {
            holiday_type.value: sum(
                1
                for holiday in items
                if holiday.holiday_type
                == holiday_type
            )
            for holiday_type in MarketHolidayType
        }

    @staticmethod
    def status_distribution(
        holidays: MarketHolidayCollection,
    ) -> dict[str, int]:
        """
        Return distribution by holiday status.
        """

        items = holidays.to_list()

        return {
            status.value: sum(
                1
                for holiday in items
                if holiday.status == status
            )
            for status in MarketHolidayStatus
        }

    @staticmethod
    def exchange_distribution(
        holidays: MarketHolidayCollection,
    ) -> dict[str, int]:
        """
        Return distribution by exchange.
        """

        distribution: dict[str, int] = {}

        for holiday in holidays.to_list():

            exchange = (
                holiday.exchange.strip().upper()
                or "UNKNOWN"
            )

            distribution[exchange] = (
                distribution.get(exchange, 0) + 1
            )

        return distribution