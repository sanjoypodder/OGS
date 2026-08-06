"""
CorporateEvent Collection
"""

from __future__ import annotations

from ogs.smart_money.base.collection import BaseCollection

from .domain import CorporateEvent
from .enums import (
    CorporateEventStatus,
    CorporateEventType,
)


class CorporateEventCollection(
    BaseCollection[CorporateEvent]
):

    def add(
        self,
        corporate_event: CorporateEvent,
    ) -> None:

        self._items.append(corporate_event)

    def find(
        self,
        corporate_event_id: str,
    ) -> CorporateEvent | None:

        for item in self._items:

            if (
                item.corporate_event_id
                == corporate_event_id
            ):
                return item

        return None

    def by_exchange(
        self,
        exchange: str,
    ) -> list[CorporateEvent]:

        return [
            item
            for item in self._items
            if item.exchange == exchange
        ]

    def by_market(
        self,
        market: str,
    ) -> list[CorporateEvent]:

        return [
            item
            for item in self._items
            if item.market == market
        ]

    def by_instrument(
        self,
        instrument: str,
    ) -> list[CorporateEvent]:

        return [
            item
            for item in self._items
            if item.instrument == instrument
        ]

    def by_event_type(
        self,
        event_type: CorporateEventType,
    ) -> list[CorporateEvent]:

        return [
            item
            for item in self._items
            if (
                item.corporate_event_type
                == event_type
            )
        ]

    def by_status(
        self,
        status: CorporateEventStatus,
    ) -> list[CorporateEvent]:

        return [
            item
            for item in self._items
            if item.status == status
        ]

    def active(
        self,
    ) -> list[CorporateEvent]:

        return [
            item
            for item in self._items
            if item.is_active
        ]

    def to_list(
        self,
    ) -> list[CorporateEvent]:

        return list(self._items)