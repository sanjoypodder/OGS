"""
OGS Smart Money AI

Quote Statistics
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseStatistics

from .collection import QuoteCollection


class QuoteStatistics(BaseStatistics):
    """
    Statistics for QuoteCollection.
    """

    def __init__(
        self,
        collection: QuoteCollection,
    ):
        self.collection = collection

    @property
    def count(self) -> int:
        """
        Total number of quotes.
        """
        return len(self.collection)

    @property
    def active_count(self) -> int:
        """
        Total active quotes.
        """
        return len(self.collection.active())

    @property
    def inactive_count(self) -> int:
        """
        Total inactive quotes.
        """
        return len(self.collection.inactive())

    @property
    def average_spread(self) -> float:
        """
        Average spread.
        """
        spreads = [
            q.spread
            for q in self.collection
        ]

        if not spreads:
            return 0.0

        return sum(spreads) / len(spreads)

    @property
    def type_distribution(self) -> dict[str, int]:
        """
        Distribution by quote type.
        """
        return dict(
            Counter(
                q.quote_type.value
                for q in self.collection
            )
        )

    @property
    def status_distribution(self) -> dict[str, int]:
        """
        Distribution by status.
        """
        return dict(
            Counter(
                q.status.value
                for q in self.collection
            )
        )

    @property
    def provider_distribution(self) -> dict[str, int]:
        """
        Distribution by provider.
        """
        return dict(
            Counter(
                q.provider
                for q in self.collection
            )
        )

    def summary(self) -> dict:
        """
        Statistics summary.
        """
        return {
            "count": self.count,
            "active": self.active_count,
            "inactive": self.inactive_count,
            "average_spread": self.average_spread,
            "type_distribution": self.type_distribution,
            "status_distribution": self.status_distribution,
            "provider_distribution": self.provider_distribution,
        }