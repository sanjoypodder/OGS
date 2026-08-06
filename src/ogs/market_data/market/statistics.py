"""
OGS Smart Money AI

Market Statistics
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseStatistics

from .collection import MarketCollection


class MarketStatistics(BaseStatistics):
    """
    Statistics for MarketCollection.
    """

    def __init__(
        self,
        collection: MarketCollection,
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
    def exchange_count(self) -> int:
        return self.collection.total_exchanges()

    @property
    def broker_count(self) -> int:
        return self.collection.total_brokers()

    @property
    def account_count(self) -> int:
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
                market.status.value
                for market in self.collection
            )
        )

    def summary(self) -> dict:
        return {
            "count": self.count,
            "open_count": self.open_count,
            "closed_count": self.closed_count,
            "exchange_count": self.exchange_count,
            "broker_count": self.broker_count,
            "account_count": self.account_count,
            "total_equity": self.total_equity,
            "total_cash": self.total_cash,
            "total_buying_power": self.total_buying_power,
            "total_margin_used": self.total_margin_used,
            "status_distribution": self.status_distribution,
        }