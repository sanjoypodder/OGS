"""
===========================================================

OGS Smart Money AI

Imbalance Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import Imbalance


class ImbalanceSeries(BaseCollection[Imbalance]):
    """
    Collection of imbalances.
    """

    def __init__(self) -> None:
        self._items: list[Imbalance] = []

    @property
    def imbalances(self) -> list[Imbalance]:
        return self._items

    def append(
        self,
        imbalance: Imbalance,
    ) -> None:
        self._items.append(imbalance)

    def latest(
        self,
        count: int = 1,
    ) -> list[Imbalance]:
        return self._items[-count:]