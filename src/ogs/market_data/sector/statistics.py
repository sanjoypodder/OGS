"""
===========================================================

OGS Smart Money AI

Sector Statistics

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.statistics import BaseStatistics

from .collection import SectorCollection
from .enums import SectorType


class SectorStatistics(
    BaseStatistics,
):

    def __init__(
        self,
        collection: SectorCollection,
    ):

        self.collection = collection

    @property
    def count(self):

        return len(self.collection)

    @property
    def active_count(self):

        return len(
            self.collection.active()
        )

    def distribution(self):

        return {
            sector_type.name: sum(
                1
                for sector in self.collection
                if sector.sector_type == sector_type
            )
            for sector_type in SectorType
        }

    def summary(self):

        return {
            "count": self.count,
            "active": self.active_count,
        }