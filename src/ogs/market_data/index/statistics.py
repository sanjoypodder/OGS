"""
===========================================================

OGS Smart Money AI

Index Statistics

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.statistics import BaseStatistics

from .collection import IndexCollection
from .enums import IndexType


class IndexStatistics(
    BaseStatistics,
):

    def __init__(
        self,
        collection: IndexCollection,
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
            index_type.name: sum(
                1
                for item in self.collection
                if item.index_type == index_type
            )
            for index_type in IndexType
        }

    def summary(self):

        return {
            "count": self.count,
            "active": self.active_count,
        }