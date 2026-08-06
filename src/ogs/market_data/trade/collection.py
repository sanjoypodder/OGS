"""
OGS Smart Money AI

Trade Collection
"""

from __future__ import annotations

from ogs.framework import BaseCollection

from .domain import Trade
from .enums import (
    TradeSide,
    TradeStatus,
)


class TradeCollection(BaseCollection[Trade]):
    """
    Collection of Trade objects.
    """

    def __init__(self, items=None):
        super().__init__(items)

    @property
    def items(self) -> list[Trade]:
        """
        Compatibility property.
        """
        return self._items

    def add(self, trade: Trade) -> None:
        self.append(trade)

    def buys(self) -> list[Trade]:
        return [
            trade
            for trade in self
            if trade.side == TradeSide.BUY
        ]

    def sells(self) -> list[Trade]:
        return [
            trade
            for trade in self
            if trade.side == TradeSide.SELL
        ]

    def filled(self) -> list[Trade]:
        return [
            trade
            for trade in self
            if trade.status == TradeStatus.FILLED
        ]

    def by_symbol(
        self,
        symbol: str,
    ) -> list[Trade]:

        return [
            trade
            for trade in self
            if trade.symbol == symbol
        ]

    def by_provider(
        self,
        provider: str,
    ) -> list[Trade]:

        return [
            trade
            for trade in self
            if trade.provider == provider
        ]

    def find(
        self,
        trade_id: str,
    ) -> Trade | None:

        return next(
            (
                trade
                for trade in self
                if trade.trade_id == trade_id
            ),
            None,
        )

    def total_value(self) -> float:
        return sum(
            trade.value
            for trade in self
        )

    def total_fees(self) -> float:
        return sum(
            trade.fees
            for trade in self
        )

    def to_list(self) -> list[dict]:
        return [
            trade.to_dict()
            for trade in self
        ]