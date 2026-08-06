"""
Settlement Collection
"""

from __future__ import annotations

from ogs.smart_money.base.collection import BaseCollection

from .domain import Settlement
from .enums import (
    SettlementCycle,
    SettlementType,
)


class SettlementCollection(
    BaseCollection[Settlement]
):

    def add(
        self,
        settlement: Settlement,
    ) -> None:

        self._items.append(settlement)

    def find(
        self,
        settlement_id: str,
    ) -> Settlement | None:

        for item in self._items:

            if item.settlement_id == settlement_id:
                return item

        return None

    def by_exchange(
        self,
        exchange: str,
    ) -> list[Settlement]:

        return [
            item
            for item in self._items
            if item.exchange == exchange
        ]

    def by_market(
        self,
        market: str,
    ) -> list[Settlement]:

        return [
            item
            for item in self._items
            if item.market == market
        ]

    def by_instrument(
        self,
        instrument: str,
    ) -> list[Settlement]:

        return [
            item
            for item in self._items
            if item.instrument == instrument
        ]

    def by_cycle(
        self,
        cycle: SettlementCycle,
    ) -> list[Settlement]:

        return [
            item
            for item in self._items
            if item.settlement_cycle == cycle
        ]

    def by_type(
        self,
        settlement_type: SettlementType,
    ) -> list[Settlement]:

        return [
            item
            for item in self._items
            if item.settlement_type == settlement_type
        ]

    def active(
        self,
    ) -> list[Settlement]:

        return [
            item
            for item in self._items
            if item.is_active
        ]

    def to_list(
        self,
    ) -> list[Settlement]:

        return list(self._items)