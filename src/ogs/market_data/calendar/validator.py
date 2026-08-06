"""
===========================================================

OGS Smart Money AI

Calendar Validator

===========================================================
"""

from __future__ import annotations

from datetime import date

from ogs.smart_money.base.validator import BaseValidator

from .domain import Calendar
from .enums import (
    CalendarStatus,
    CalendarType,
)


class CalendarValidator(
    BaseValidator[Calendar],
):
    """
    Calendar Validator.
    """

    def validate(
        self,
        value: Calendar,
    ) -> None:

        if not value.calendar_id.strip():
            raise ValueError("Invalid calendar_id.")

        if not value.exchange.strip():
            raise ValueError("Invalid exchange.")

        if not value.market.strip():
            raise ValueError("Invalid market.")

        if value.trading_date is None:
            raise ValueError("Trading date required.")

        if not isinstance(
            value.trading_date,
            date,
        ):
            raise ValueError("Invalid trading date.")

        if not isinstance(
            value.calendar_type,
            CalendarType,
        ):
            raise ValueError("Invalid calendar type.")

        if not isinstance(
            value.status,
            CalendarStatus,
        ):
            raise ValueError("Invalid calendar status.")