"""
===========================================================

OGS Smart Money AI

Buy Side Liquidity Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import BuySideLiquidity


class BuySideLiquiditySeries(
    BaseCollection[BuySideLiquidity]
):
    """
    Collection of Buy-Side Liquidity pools.
    """

    @property
    def pools(self):

        return self._items

    def append(
        self,
        pool: BuySideLiquidity,
    ):

        self._items.append(pool)

    def latest(
        self,
        count: int,
    ):

        return BuySideLiquiditySeries(
            self._items[-count:]
        )