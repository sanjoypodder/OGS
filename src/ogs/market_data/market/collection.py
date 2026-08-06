"""
OGS Smart Money AI

Market Collection
"""

from __future__ import annotations

from ogs.framework import BaseCollection

from .domain import Market
from .enums import MarketStatus


class MarketCollection(BaseCollection[Market]):
    """
    Collection of Market objects.
    """

    def __init__(self, items=None):
        super().__init__(items)

    @property
    def items(self) -> list[Market]:
        return self._items

    def add(
        self,
        market: Market,
    ) -> None:
        self.append(market)

    def open(self) -> list[Market]:
        return [
            market
            for market in self
            if market.status == MarketStatus.OPEN
        ]

    def closed(self) -> list[Market]:
        return [
            market
            for market in self
            if market.status == MarketStatus.CLOSED
        ]

    def find(
        self,
        market_id: str,
    ) -> Market | None:
        return next(
            (
                market
                for market in self
                if market.market_id == market_id
            ),
            None,
        )

    def total_exchanges(self) -> int:
        return sum(
            market.exchange_count
            for market in self
        )

    def total_brokers(self) -> int:
        return sum(
            market.broker_count
            for market in self
        )

    def total_accounts(self) -> int:
        return sum(
            market.account_count
            for market in self
        )

    def total_equity(self) -> float:
        return sum(
            market.total_equity
            for market in self
        )

    def total_cash(self) -> float:
        return sum(
            market.total_cash
            for market in self
        )

    def total_buying_power(self) -> float:
        return sum(
            market.total_buying_power
            for market in self
        )

    def total_margin_used(self) -> float:
        return sum(
            market.total_margin_used
            for market in self
        )

    def to_list(self) -> list[dict]:
        return [
            market.to_dict()
            for market in self
        ]