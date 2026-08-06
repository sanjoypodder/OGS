"""
OGS Smart Money AI

Exchange Collection
"""

from __future__ import annotations

from ogs.framework import BaseCollection

from .domain import Exchange
from .enums import ExchangeStatus


class ExchangeCollection(BaseCollection[Exchange]):
    """
    Collection of Exchange objects.
    """

    def __init__(self, items=None):
        super().__init__(items)

    @property
    def items(self) -> list[Exchange]:
        return self._items

    def add(
        self,
        exchange: Exchange,
    ) -> None:
        self.append(exchange)

    def open(self) -> list[Exchange]:
        return [
            exchange
            for exchange in self
            if exchange.status == ExchangeStatus.OPEN
        ]

    def closed(self) -> list[Exchange]:
        return [
            exchange
            for exchange in self
            if exchange.status == ExchangeStatus.CLOSED
        ]

    def find(
        self,
        exchange_id: str,
    ) -> Exchange | None:

        return next(
            (
                exchange
                for exchange in self
                if exchange.exchange_id == exchange_id
            ),
            None,
        )

    def total_brokers(self) -> int:
        return sum(
            exchange.broker_count
            for exchange in self
        )

    def total_accounts(self) -> int:
        return sum(
            exchange.account_count
            for exchange in self
        )

    def total_equity(self) -> float:
        return sum(
            exchange.total_equity
            for exchange in self
        )

    def total_cash(self) -> float:
        return sum(
            exchange.total_cash
            for exchange in self
        )

    def total_buying_power(self) -> float:
        return sum(
            exchange.total_buying_power
            for exchange in self
        )

    def total_margin_used(self) -> float:
        return sum(
            exchange.total_margin_used
            for exchange in self
        )

    def to_list(self) -> list[dict]:
        return [
            exchange.to_dict()
            for exchange in self
        ]