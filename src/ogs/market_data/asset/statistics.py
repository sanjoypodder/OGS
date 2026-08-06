"""
OGS Smart Money AI

Asset Statistics
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseStatistics

from .collection import AssetCollection


class AssetStatistics(BaseStatistics):
    """
    Statistics for AssetCollection.
    """

    def __init__(
        self,
        collection: AssetCollection,
    ):
        self.collection = collection

    @property
    def count(self) -> int:
        return len(self.collection)

    @property
    def active_count(self) -> int:
        return len(self.collection.active())

    @property
    def inactive_count(self) -> int:
        return len(self.collection.inactive())

    @property
    def equity_count(self) -> int:
        return len(self.collection.equities())

    @property
    def crypto_count(self) -> int:
        return len(self.collection.crypto())

    @property
    def forex_count(self) -> int:
        return len(self.collection.forex())

    @property
    def commodity_count(self) -> int:
        return len(self.collection.commodities())

    @property
    def distribution(self) -> dict[str, int]:
        return dict(
            Counter(
                asset.asset_type.value
                for asset in self.collection
            )
        )

    def summary(self) -> dict:
        return {
            "count": self.count,
            "active_count": self.active_count,
            "inactive_count": self.inactive_count,
            "equity_count": self.equity_count,
            "crypto_count": self.crypto_count,
            "forex_count": self.forex_count,
            "commodity_count": self.commodity_count,
            "distribution": self.distribution,
        }