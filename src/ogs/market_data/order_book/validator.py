"""
OGS Smart Money AI

OrderBook Validator
"""

from __future__ import annotations

from datetime import datetime

from ogs.framework import BaseValidator

from .domain import OrderBook
from .enums import (
    OrderBookStatus,
    OrderBookType,
)


class OrderBookValidator(BaseValidator):
    """
    Validates OrderBook objects.
    """

    def validate(self, orderbook: OrderBook) -> bool:

        if not isinstance(orderbook, OrderBook):
            raise TypeError("Expected OrderBook.")

        if not orderbook.name:
            raise ValueError("Name cannot be empty.")

        if not isinstance(
            orderbook.orderbook_type,
            OrderBookType,
        ):
            raise ValueError("Invalid OrderBookType.")

        if not isinstance(
            orderbook.status,
            OrderBookStatus,
        ):
            raise ValueError("Invalid OrderBookStatus.")

        if orderbook.best_bid < 0:
            raise ValueError("Negative bid.")

        if orderbook.best_ask < 0:
            raise ValueError("Negative ask.")

        if orderbook.best_ask < orderbook.best_bid:
            raise ValueError(
                "Ask must be greater than or equal to bid."
            )

        if not isinstance(orderbook.timestamp, datetime):
            raise ValueError("Invalid timestamp.")

        return True

    def __call__(self, orderbook: OrderBook) -> bool:
        return self.validate(orderbook)