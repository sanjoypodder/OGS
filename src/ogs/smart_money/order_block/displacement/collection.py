"""
===========================================================

OGS Smart Money AI

Displacement Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseCollection

from .domain import Displacement


class DisplacementSeries(
    BaseCollection[Displacement],
):
    """
    Collection of institutional
    displacement events.
    """

    @property
    def displacements(self):

        return self._items

    def append(
        self,
        displacement: Displacement,
    ):

        self._items.append(
            displacement,
        )

    def latest(
        self,
        count: int,
    ):

        return DisplacementSeries(
            self._items[-count:]
        )