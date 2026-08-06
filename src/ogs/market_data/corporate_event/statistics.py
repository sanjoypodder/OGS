"""
CorporateEvent Statistics
"""

from __future__ import annotations

from ogs.smart_money.base.statistics import BaseStatistics

from .collection import CorporateEventCollection
from .enums import (
    CorporateEventStatus,
    CorporateEventType,
)


class CorporateEventStatistics(
    BaseStatistics
):

    def __init__(
        self,
        collection: CorporateEventCollection,
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

    def event_type_distribution(self):

        return {
            event_type.name: sum(
                1
                for item in self.collection
                if (
                    item.corporate_event_type
                    == event_type
                )
            )
            for event_type in CorporateEventType
        }

    def status_distribution(self):

        return {
            status.name: sum(
                1
                for item in self.collection
                if item.status == status
            )
            for status in CorporateEventStatus
        }

    def summary(self):

        return {
            "count": self.count,
            "active": self.active_count,
        }