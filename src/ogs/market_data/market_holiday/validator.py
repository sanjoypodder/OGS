"""
OGS Smart Money AI

MarketHoliday Validator
"""

from __future__ import annotations

from ogs.smart_money.base.validator import BaseValidator

from .domain import MarketHoliday
from .enums import (
    MarketHolidayStatus,
    MarketHolidayType,
)


class MarketHolidayValidator(
    BaseValidator[MarketHoliday]
):
    """
    Validator for MarketHoliday entities.
    """

    def validate(
        self,
        value: MarketHoliday,
    ) -> None:

        if not isinstance(
            value,
            MarketHoliday,
        ):
            raise ValueError(
                "Invalid market holiday object."
            )

        if not value.market_holiday_id.strip():
            raise ValueError(
                "Invalid market holiday id."
            )

        if not value.name.strip():
            raise ValueError(
                "Invalid market holiday name."
            )

        if value.holiday_date is None:
            raise ValueError(
                "Invalid holiday date."
            )

        if not isinstance(
            value.holiday_type,
            MarketHolidayType,
        ):
            raise ValueError(
                "Invalid market holiday type."
            )

        if not isinstance(
            value.status,
            MarketHolidayStatus,
        ):
            raise ValueError(
                "Invalid market holiday status."
            )