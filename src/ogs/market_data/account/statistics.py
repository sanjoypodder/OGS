"""
OGS Smart Money AI

Account Statistics
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseStatistics

from .collection import AccountCollection


class AccountStatistics(BaseStatistics):
    """
    Statistics for AccountCollection.
    """

    def __init__(
        self,
        collection: AccountCollection,
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
    def live_count(self) -> int:
        return len(self.collection.live())

    @property
    def paper_count(self) -> int:
        return len(self.collection.paper())

    @property
    def backtest_count(self) -> int:
        return len(self.collection.backtest())

    @property
    def total_equity(self) -> float:
        return self.collection.total_equity()

    @property
    def total_cash(self) -> float:
        return self.collection.total_cash()

    @property
    def total_market_value(self) -> float:
        return self.collection.total_market_value()

    @property
    def total_realized_pnl(self) -> float:
        return self.collection.total_realized_pnl()

    @property
    def total_unrealized_pnl(self) -> float:
        return self.collection.total_unrealized_pnl()

    @property
    def total_pnl(self) -> float:
        return self.collection.total_pnl()

    @property
    def average_return(self) -> float:

        if len(self.collection) == 0:
            return 0.0

        return (
            sum(
                account.return_percentage
                for account in self.collection
            )
            / len(self.collection)
        )

    @property
    def status_distribution(self) -> dict[str, int]:
        return dict(
            Counter(
                account.status.value
                for account in self.collection
            )
        )

    @property
    def type_distribution(self) -> dict[str, int]:
        return dict(
            Counter(
                account.account_type.value
                for account in self.collection
            )
        )

    def summary(self) -> dict:

        return {
            "count": self.count,
            "active_count": self.active_count,
            "inactive_count": self.inactive_count,
            "live_count": self.live_count,
            "paper_count": self.paper_count,
            "backtest_count": self.backtest_count,
            "total_equity": self.total_equity,
            "total_cash": self.total_cash,
            "total_market_value": self.total_market_value,
            "total_realized_pnl": self.total_realized_pnl,
            "total_unrealized_pnl": self.total_unrealized_pnl,
            "total_pnl": self.total_pnl,
            "average_return": self.average_return,
            "status_distribution": self.status_distribution,
            "type_distribution": self.type_distribution,
        }