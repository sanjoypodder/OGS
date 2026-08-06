"""
===========================================================

OGS Smart Money AI

Industry Statistics

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.statistics import BaseStatistics

from .collection import IndustryCollection
from .enums import IndustryType


class IndustryStatistics(
    BaseStatistics,
):

    def __init__(
        self,
        collection: IndustryCollection,
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
            industry_type.name: sum(
                1
                for industry in self.collection
                if (
                    industry.industry_type
                    == industry_type
                )
            )
            for industry_type
            in IndustryType
        }

    def summary(self):

        return {
            "count": self.count,
            "active": self.active_count,
        }