"""
===========================================================

OGS Smart Money AI

Corporate Action Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.collection import BaseCollection

from .domain import CorporateAction
from .enums import (
    CorporateActionStatus,
    CorporateActionType,
)


class CorporateActionCollection(
    BaseCollection[CorporateAction],
):

    @property
    def items(self):

        return self._items

    def add(
        self,
        action: CorporateAction,
    ) -> None:

        self._items.append(action)

    def find(
        self,
        action_id: str,
    ) -> CorporateAction | None:

        for action in self._items:
            if action.action_id == action_id:
                return action

        return None

    def dividends(self):

        return [
            action
            for action in self._items
            if action.action_type
            == CorporateActionType.DIVIDEND
        ]

    def effective(self):

        return [
            action
            for action in self._items
            if action.status
            == CorporateActionStatus.EFFECTIVE
        ]

    def to_list(self):

        return list(self._items)