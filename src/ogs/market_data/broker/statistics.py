"""
OGS Smart Money AI

Broker Statistics
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseStatistics

from .collection import BrokerCollection


class BrokerStatistics(BaseStatistics):
    """
    Statistics for BrokerCollection.
    """

    def __init__(
        self,
        collection: BrokerCollection,
    ):
        self.collection = collection

    @property
    def count(self) -> int:
        return len(self.collection)

    @property
    def active_count(self) -> int:
        return len(self.collection.active())

    @property
    def inactive_count(self) -> int:
        return len(self.collection.inactive())

    @property
    def total_accounts(self) -> int:
        return self.collection.total_accounts()

    @property
    def total_equity(self) -> float:
        return self.collection.total_equity()

    @property
    def total_cash(self) -> float:
        return self.collection.total_cash()

    @property
    def total_buying_power(self) -> float:
        return self.collection.total_buying_power()

    @property
    def total_margin_used(self) -> float:
        return self.collection.total_margin_used()

    @property
    def status_distribution(self) -> dict[str, int]:
        return dict(
            Counter(
                broker.status.value
                for broker in self.collection
            )
        )

    def summary(self) -> dict:
        return {
            "count": self.count,
            "active_count": self.active_count,
            "inactive_count": self.inactive_count,
            "total_accounts": self.total_accounts,
            "total_equity": self.total_equity,
            "total_cash": self.total_cash,
            "total_buying_power": self.total_buying_power,
            "total_margin_used": self.total_margin_used,
            "status_distribution": self.status_distribution,
        }