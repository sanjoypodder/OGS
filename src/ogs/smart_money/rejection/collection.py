"""
===========================================================

OGS Smart Money AI

Rejection Block Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import RejectionBlock


class RejectionBlockSeries(BaseCollection[RejectionBlock]):
    """
    Collection of Rejection Blocks.
    """

    def __init__(self) -> None:
        self._items: list[RejectionBlock] = []

    @property
    def rejection_blocks(self) -> list[RejectionBlock]:
        return self._items

    def append(
        self,
        rejection_block: RejectionBlock,
    ) -> None:
        self._items.append(rejection_block)

    def latest(
        self,
        count: int = 1,
    ) -> list[RejectionBlock]:
        return self._items[-count:]