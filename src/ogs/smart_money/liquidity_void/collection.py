"""
===========================================================

OGS Smart Money AI

Liquidity Void Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import LiquidityVoid


class LiquidityVoidSeries(BaseCollection[LiquidityVoid]):
    """
    Collection of Liquidity Voids.
    """

    def __init__(self) -> None:
        self._items: list[LiquidityVoid] = []

    @property
    def liquidity_voids(self) -> list[LiquidityVoid]:
        return self._items

    def append(
        self,
        liquidity_void: LiquidityVoid,
    ) -> None:
        self._items.append(liquidity_void)

    def latest(
        self,
        count: int = 1,
    ) -> list[LiquidityVoid]:
        return self._items[-count:]