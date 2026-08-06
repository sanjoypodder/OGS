"""
===========================================================

OGS Smart Money AI

Breaker Block Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import BreakerBlock


class BreakerBlockSeries(BaseCollection[BreakerBlock]):
    """
    Collection of Breaker Blocks.
    """

    def __init__(self) -> None:
        self._items: list[BreakerBlock] = []

    @property
    def breaker_blocks(self) -> list[BreakerBlock]:
        return self._items

    def append(
        self,
        breaker_block: BreakerBlock,
    ) -> None:
        self._items.append(breaker_block)

    def latest(
        self,
        count: int = 1,
    ) -> list[BreakerBlock]:
        return self._items[-count:]