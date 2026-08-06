"""
===========================================================

OGS Smart Money AI

Order Block Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import OrderBlock


class OrderBlockSeries(
    BaseCollection[OrderBlock]
):
    """
    Collection of Order Blocks.
    """

    @property
    def order_blocks(self):

        return self._items

    def append(
        self,
        order_block: OrderBlock,
    ):

        self._items.append(order_block)

    def latest(
        self,
        count: int,
    ):

        return OrderBlockSeries(
            self._items[-count:]
        )