"""
TradingHours Collection
"""

from __future__ import annotations

from ogs.smart_money.base.collection import BaseCollection

from .domain import TradingHours
from .enums import TradingHoursType


class TradingHoursCollection(
    BaseCollection[TradingHours]
):

    def add(
        self,
        item: TradingHours,
    ):

        self._items.append(item)

    def find(
        self,
        trading_hours_id: str,
    ):

        for item in self._items:

            if (
                item.trading_hours_id
                == trading_hours_id
            ):
                return item

        return None

    def by_exchange(
        self,
        exchange: str,
    ):

        return [
            x
            for x in self._items
            if x.exchange == exchange
        ]

    def by_market(
        self,
        market: str,
    ):

        return [
            x
            for x in self._items
            if x.market == market
        ]

    def by_type(
        self,
        trading_hours_type: TradingHoursType,
    ):

        return [
            x
            for x in self._items
            if (
                x.trading_hours_type
                == trading_hours_type
            )
        ]

    def active(self):

        return [
            x
            for x in self._items
            if x.is_active
        ]

    def to_list(self):

        return list(self._items)