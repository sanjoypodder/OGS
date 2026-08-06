"""
===========================================================

OGS Smart Money AI

Calendar Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.collection import BaseCollection

from .domain import Calendar
from .enums import (
    CalendarStatus,
    CalendarType,
)


class CalendarCollection(
    BaseCollection[Calendar],
):

    @property
    def items(self):

        return self._items

    def add(
        self,
        calendar: Calendar,
    ) -> None:

        self._items.append(calendar)

    def find(
        self,
        calendar_id: str,
    ) -> Calendar | None:

        for calendar in self._items:
            if calendar.calendar_id == calendar_id:
                return calendar

        return None

    def trading_days(self):

        return [
            c
            for c in self._items
            if c.calendar_type == CalendarType.TRADING_DAY
        ]

    def holidays(self):

        return [
            c
            for c in self._items
            if c.calendar_type == CalendarType.HOLIDAY
        ]

    def open_days(self):

        return [
            c
            for c in self._items
            if c.status == CalendarStatus.OPEN
        ]

    def to_list(self):

        return list(self._items)