"""
===========================================================

OGS Smart Money AI

Metadata Statistics

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base.statistics import (
    BaseStatistics,
)

from .collection import MetadataCollection
from .enums import (
    MetadataType,
    MetadataValueType,
)


class MetadataStatistics(
    BaseStatistics,
):

    def __init__(
        self,
        collection: MetadataCollection,
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

    def entity_distribution(self):

        result = {}

        for item in self.collection:
            result[item.entity_type] = (
                result.get(
                    item.entity_type,
                    0,
                )
                + 1
            )

        return result

    def metadata_distribution(self):

        return {
            metadata_type.name: sum(
                1
                for item in self.collection
                if (
                    item.metadata_type
                    == metadata_type
                )
            )
            for metadata_type in MetadataType
        }

    def value_distribution(self):

        return {
            value_type.name: sum(
                1
                for item in self.collection
                if (
                    item.value_type
                    == value_type
                )
            )
            for value_type in MetadataValueType
        }

    def summary(self):

        return {
            "count": self.count,
            "active": self.active_count,
        }