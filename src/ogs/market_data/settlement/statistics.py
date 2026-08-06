"""
Settlement Statistics
"""

from __future__ import annotations

from ogs.smart_money.base.statistics import BaseStatistics

from .collection import SettlementCollection
from .enums import (
    SettlementCycle,
    SettlementType,
)


class SettlementStatistics(
    BaseStatistics
):

    def __init__(
        self,
        collection: SettlementCollection,
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
                result.get(item.exchange, 0)
                + 1
            )

        return result

    def market_distribution(self):

        result = {}

        for item in self.collection:
            result[item.market] = (
                result.get(item.market, 0)
                + 1
            )

        return result

    def cycle_distribution(self):

        return {
            cycle.name: sum(
                1
                for item in self.collection
                if item.settlement_cycle == cycle
            )
            for cycle in SettlementCycle
        }

    def type_distribution(self):

        return {
            settlement_type.name: sum(
                1
                for item in self.collection
                if item.settlement_type == settlement_type
            )
            for settlement_type in SettlementType
        }

    def summary(self):

        return {
            "count": self.count,
            "active": self.active_count,
        }