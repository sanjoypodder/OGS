"""
OGS Smart Money AI

OrderBook Factory
"""

from __future__ import annotations

from copy import deepcopy

from ogs.framework import BaseFactory

from .domain import OrderBook
from .enums import OrderBookType
from .validator import OrderBookValidator


class OrderBookFactory(BaseFactory):
    """
    Factory for creating OrderBook objects.
    """

    validator = OrderBookValidator()

    @classmethod
    def create(cls, **kwargs) -> OrderBook:

        orderbook = OrderBook(**kwargs)

        cls.validator(orderbook)

        return orderbook

    @classmethod
    def live(cls, **kwargs) -> OrderBook:

        kwargs["orderbook_type"] = OrderBookType.LIVE

        return cls.create(**kwargs)

    @classmethod
    def historical(cls, **kwargs) -> OrderBook:

        kwargs["orderbook_type"] = OrderBookType.HISTORICAL

        return cls.create(**kwargs)

    @classmethod
    def simulated(cls, **kwargs) -> OrderBook:

        kwargs["orderbook_type"] = OrderBookType.SIMULATED

        return cls.create(**kwargs)

    @classmethod
    def clone(
        cls,
        orderbook: OrderBook,
    ) -> OrderBook:

        clone = deepcopy(orderbook)

        cls.validator(clone)

        return clone