"""
===========================================================

OGS Smart Money AI

Mitigation Block Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import MitigationBlock


class MitigationBlockSeries(BaseCollection[MitigationBlock]):
    """
    Collection of Mitigation Blocks.
    """

    def __init__(self) -> None:
        self._items: list[MitigationBlock] = []

    @property
    def mitigation_blocks(self) -> list[MitigationBlock]:
        return self._items

    def append(
        self,
        mitigation_block: MitigationBlock,
    ) -> None:
        self._items.append(mitigation_block)

    def latest(
        self,
        count: int = 1,
    ) -> list[MitigationBlock]:
        return self._items[-count:]