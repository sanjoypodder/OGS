"""
===========================================================

OGS Smart Money AI

Calendar Factory

===========================================================
"""

from __future__ import annotations

from copy import deepcopy
from datetime import date

from .domain import Calendar
from .enums import (
    CalendarStatus,
    CalendarType,
)


class CalendarFactory:
    """
    Calendar Factory.
    """

    @staticmethod
    def create(
        calendar_id: str,
        exchange: str,
        market: str,
        trading_date: date,
        **kwargs,
    ) -> Calendar:

        return Calendar(
            calendar_id=calendar_id,
            exchange=exchange,
            market=market,
            trading_date=trading_date,
            **kwargs,
        )

    @staticmethod
    def trading_day(
        calendar_id: str,
        exchange: str,
        market: str,
        trading_date: date,
        **kwargs,
    ) -> Calendar:

        return Calendar(
            calendar_id=calendar_id,
            exchange=exchange,
            market=market,
            trading_date=trading_date,
            calendar_type=CalendarType.TRADING_DAY,
            status=CalendarStatus.OPEN,
            **kwargs,
        )

    @staticmethod
    def clone(
        calendar: Calendar,
    ) -> Calendar:

        return deepcopy(calendar)