"""
OGS Smart Money AI

Trade Validator
"""

from __future__ import annotations

from datetime import datetime

from ogs.framework import BaseValidator

from .domain import Trade
from .enums import (
    TradeSide,
    TradeStatus,
)


class TradeValidator(BaseValidator):
    """
    Validator for Trade objects.
    """

    def validate(self, trade: Trade) -> bool:

        if not isinstance(trade, Trade):
            raise TypeError("Expected Trade.")

        if not trade.trade_id:
            raise ValueError("Trade ID cannot be empty.")

        if not isinstance(trade.side, TradeSide):
            raise ValueError("Invalid TradeSide.")

        if not isinstance(trade.status, TradeStatus):
            raise ValueError("Invalid TradeStatus.")

        if trade.price < 0:
            raise ValueError("Price cannot be negative.")

        if trade.quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        if trade.fees < 0:
            raise ValueError("Fees cannot be negative.")

        if not isinstance(trade.timestamp, datetime):
            raise ValueError("Invalid timestamp.")

        return True

    def __call__(self, trade: Trade) -> bool:
        return self.validate(trade)