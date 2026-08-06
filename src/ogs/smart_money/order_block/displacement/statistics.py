"""
===========================================================

OGS Smart Money AI

Displacement Statistics

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseStatistics

from .collection import DisplacementSeries
from .enums import DisplacementDirection


class DisplacementStatistics(
    BaseStatistics,
):
    """
    Statistics for displacement events.
    """

    def __init__(
        self,
        displacements: DisplacementSeries,
    ):

        self._displacements = displacements

    @property
    def total(self) -> int:

        return len(self._displacements)

    @property
    def bullish(self) -> int:

        return sum(
            1
            for displacement in self._displacements
            if displacement.direction
            == DisplacementDirection.BULLISH
        )

    @property
    def bearish(self) -> int:

        return sum(
            1
            for displacement in self._displacements
            if displacement.direction
            == DisplacementDirection.BEARISH
        )