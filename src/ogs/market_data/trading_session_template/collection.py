"""
TradingSessionTemplate Collection
"""

from __future__ import annotations

from ogs.smart_money.base.collection import BaseCollection

from .domain import TradingSessionTemplate
from .enums import TradingSessionTemplateType


class TradingSessionTemplateCollection(
    BaseCollection[TradingSessionTemplate]
):

    def add(
        self,
        session: TradingSessionTemplate,
    ) -> None:

        self._items.append(session)

    def find(
        self,
        template_id: str,
    ) -> TradingSessionTemplate | None:

        for item in self._items:
            if (
                item.trading_session_template_id
                == template_id
            ):
                return item

        return None

    def by_exchange(
        self,
        exchange: str,
    ) -> list[TradingSessionTemplate]:

        return [
            item
            for item in self._items
            if item.exchange == exchange
        ]

    def by_market(
        self,
        market: str,
    ) -> list[TradingSessionTemplate]:

        return [
            item
            for item in self._items
            if item.market == market
        ]

    def by_session_type(
        self,
        session_type: TradingSessionTemplateType,
    ) -> list[TradingSessionTemplate]:

        return [
            item
            for item in self._items
            if item.session_type == session_type
        ]

    def active(
        self,
    ) -> list[TradingSessionTemplate]:

        return [
            item
            for item in self._items
            if item.is_active
        ]

    def to_list(
        self,
    ) -> list[TradingSessionTemplate]:

        return list(self._items)