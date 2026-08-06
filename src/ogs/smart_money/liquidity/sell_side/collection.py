"""
===========================================================

OGS Smart Money AI

Sell Side Liquidity Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import SellSideLiquidity


class SellSideLiquiditySeries(
    BaseCollection[SellSideLiquidity]
):
    """
    Collection of Sell-Side Liquidity pools.
    """

    @property
    def pools(self):

        return self._items

    def append(
        self,
        pool: SellSideLiquidity,
    ):

        self._items.append(pool)

    def latest(
        self,
        count: int,
    ):

        return SellSideLiquiditySeries(
            self._items[-count:]
        )