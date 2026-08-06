"""
OGS Smart Money AI

Exchange Statistics
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseStatistics

from .collection import ExchangeCollection


class ExchangeStatistics(BaseStatistics):
    """
    Statistics for ExchangeCollection.
    """

    def __init__(
        self,
        collection: ExchangeCollection,
    ):
        self.collection = collection

    @property
    def count(self) -> int:
        return len(self.collection)

    @property
    def open_count(self) -> int:
        return len(self.collection.open())

    @property
    def closed_count(self) -> int:
        return len(self.collection.closed())

    @property
    def total_brokers(self) -> int:
        return self.collection.total_brokers()

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
                exchange.status.value
                for exchange in self.collection
            )
        )

    def summary(self) -> dict:
        return {
            "count": self.count,
            "open_count": self.open_count,
            "closed_count": self.closed_count,
            "total_brokers": self.total_brokers,
            "total_accounts": self.total_accounts,
            "total_equity": self.total_equity,
            "total_cash": self.total_cash,
            "total_buying_power": self.total_buying_power,
            "total_margin_used": self.total_margin_used,
            "status_distribution": self.status_distribution,
        }