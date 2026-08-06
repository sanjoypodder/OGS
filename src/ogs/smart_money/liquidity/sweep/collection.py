"""
===========================================================

OGS Smart Money AI

Liquidity Sweep Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import LiquiditySweep


class LiquiditySweepSeries(
    BaseCollection[LiquiditySweep]
):
    """
    Collection of Liquidity Sweeps.
    """

    @property
    def sweeps(self):

        return self._items

    def append(
        self,
        sweep: LiquiditySweep,
    ):

        self._items.append(sweep)

    def latest(
        self,
        count: int,
    ):

        return LiquiditySweepSeries(
            self._items[-count:]
        )