"""
===========================================================

OGS Smart Money AI

Market Structure Collection

===========================================================
"""

from __future__ import annotations

from collections.abc import Iterable

from ogs.smart_money.base import BaseCollection

from .domain import SwingPoint


class SwingSeries(
    BaseCollection[SwingPoint],
):
    """
    Collection of Swing Points.
    """

    def __init__(
        self,
        items: Iterable[SwingPoint] | None = None,
    ) -> None:

        super().__init__(items)

    def append(
        self,
        swing: SwingPoint,
    ) -> None:
        """
        Append a swing point.
        """

        self._items.append(swing)

    def latest(
        self,
        count: int = 1,
    ) -> list[SwingPoint]:
        """
        Return latest swing points.
        """

        return self._items[-count:]