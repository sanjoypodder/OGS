"""
TradingHours Statistics
"""

from __future__ import annotations

from ogs.smart_money.base.statistics import BaseStatistics

from .collection import TradingHoursCollection
from .enums import TradingHoursType


class TradingHoursStatistics(
    BaseStatistics
):

    def __init__(
        self,
        collection: TradingHoursCollection,
    ):

        self.collection = collection

    @property
    def count(self):

        return len(self.collection)

    @property
    def active_count(self):

        return len(
            self.collection.active()
        )

    def exchange_distribution(self):

        result = {}

        for item in self.collection:
            result[item.exchange] = (
                result.get(
                    item.exchange,
                    0,
                )
                + 1
            )

        return result

    def market_distribution(self):

        result = {}

        for item in self.collection:
            result[item.market] = (
                result.get(
                    item.market,
                    0,
                )
                + 1
            )

        return result

    def type_distribution(self):

        return {
            t.name: sum(
                1
                for item in self.collection
                if (
                    item.trading_hours_type
                    == t
                )
            )
            for t in TradingHoursType
        }

    def summary(self):

        return {
            "count": self.count,
            "active": self.active_count,
        }