"""
OGS Smart Money AI

Trade Factory
"""

from __future__ import annotations

from copy import deepcopy

from ogs.framework import BaseFactory

from .domain import Trade
from .enums import (
    TradeSide,
    TradeStatus,
)
from .validator import TradeValidator


class TradeFactory(BaseFactory):
    """
    Factory for creating Trade objects.
    """

    validator = TradeValidator()

    @classmethod
    def create(cls, **kwargs) -> Trade:

        trade = Trade(**kwargs)

        cls.validator(trade)

        return trade

    @classmethod
    def buy(cls, **kwargs) -> Trade:

        kwargs["side"] = TradeSide.BUY
        kwargs.setdefault("status", TradeStatus.FILLED)

        return cls.create(**kwargs)

    @classmethod
    def sell(cls, **kwargs) -> Trade:

        kwargs["side"] = TradeSide.SELL
        kwargs.setdefault("status", TradeStatus.FILLED)

        return cls.create(**kwargs)

    @classmethod
    def clone(cls, trade: Trade) -> Trade:

        clone = deepcopy(trade)

        cls.validator(clone)

        return clone