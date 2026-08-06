"""
===========================================================

OGS Smart Money AI

Sector Collection

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.collection import BaseCollection

from .domain import Sector
from .enums import SectorType


class SectorCollection(
    BaseCollection[Sector],
):

    @property
    def items(self):

        return self._items

    def add(
        self,
        sector: Sector,
    ) -> None:

        self._items.append(sector)

    def find(
        self,
        sector_code: str,
    ) -> Sector | None:

        for sector in self._items:

            if sector.sector_code == sector_code:
                return sector

        return None

    def by_type(
        self,
        sector_type: SectorType,
    ):

        return [
            sector
            for sector in self._items
            if sector.sector_type == sector_type
        ]

    def active(self):

        return [
            sector
            for sector in self._items
            if sector.is_active
        ]

    def to_list(self):

        return list(self._items)