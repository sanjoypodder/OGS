"""
===========================================================

OGS Smart Money AI

Calendar Statistics

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.statistics import BaseStatistics

from .collection import CalendarCollection
from .enums import CalendarType


class CalendarStatistics(
    BaseStatistics,
):

    def __init__(
        self,
        collection: CalendarCollection,
    ):

        self.collection = collection

    @property
    def count(self):

        return len(self.collection)

    @property
    def trading_day_count(self):

        return len(self.collection.trading_days())

    @property
    def holiday_count(self):

        return len(self.collection.holidays())

    @property
    def open_count(self):

        return len(self.collection.open_days())

    def distribution(self):

        return {
            calendar_type.name: sum(
                1
                for calendar in self.collection
                if calendar.calendar_type == calendar_type
            )
            for calendar_type in CalendarType
        }

    def summary(self):

        return {
            "count": self.count,
            "trading_days": self.trading_day_count,
            "holidays": self.holiday_count,
            "open_days": self.open_count,
        }