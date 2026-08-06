"""
OGS Smart Money AI

OrderBook Collection
"""

from __future__ import annotations

from ogs.framework import BaseCollection

from .domain import OrderBook
from .enums import (
    OrderBookStatus,
    OrderBookType,
)


class OrderBookCollection(BaseCollection[OrderBook]):
    """
    Collection of OrderBook objects.
    """

    def __init__(self, items=None):
        super().__init__(items)

    @property
    def items(self) -> list[OrderBook]:
        """
        Compatibility property.
        """
        return self._items

    def add(self, orderbook: OrderBook) -> None:
        """
        Add an OrderBook.
        """
        self.append(orderbook)

    def active(self) -> list[OrderBook]:
        return [
            ob
            for ob in self
            if ob.status == OrderBookStatus.ACTIVE
        ]

    def inactive(self) -> list[OrderBook]:
        return [
            ob
            for ob in self
            if ob.status != OrderBookStatus.ACTIVE
        ]

    def by_type(
        self,
        orderbook_type: OrderBookType,
    ) -> list[OrderBook]:

        return [
            ob
            for ob in self
            if ob.orderbook_type == orderbook_type
        ]

    def by_provider(
        self,
        provider: str,
    ) -> list[OrderBook]:

        return [
            ob
            for ob in self
            if ob.provider == provider
        ]

    def by_symbol(
        self,
        symbol: str,
    ) -> list[OrderBook]:

        return [
            ob
            for ob in self
            if ob.symbol == symbol
        ]

    def find(
        self,
        name: str,
    ) -> OrderBook | None:

        return next(
            (
                ob
                for ob in self
                if ob.name == name
            ),
            None,
        )

    def total_active(self) -> int:
        return len(self.active())

    def to_list(self) -> list[dict]:
        return [
            ob.to_dict()
            for ob in self
        ]