"""
OGS Smart Money AI

Feed Statistics
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseStatistics

from .collection import FeedCollection


class FeedStatistics(BaseStatistics):
    """
    Feed statistics.
    """

    def __init__(
        self,
        feeds: FeedCollection,
    ):
        self.feeds = feeds

    @property
    def count(self) -> int:
        return len(self.feeds)

    @property
    def connected_count(self) -> int:
        return len(self.feeds.connected())

    @property
    def average_latency(self) -> float:
        return self.feeds.average_latency()

    @property
    def total_updates(self) -> int:
        return self.feeds.total_updates()

    @property
    def fastest_feed(self):
        return self.feeds.fastest()

    @property
    def slowest_feed(self):
        return self.feeds.slowest()

    @property
    def feed_distribution(self) -> dict[str, int]:
        return dict(
            Counter(
                feed.feed_type.value
                for feed in self.feeds
            )
        )

    @property
    def provider_distribution(self) -> dict[str, int]:
        return dict(
            Counter(
                feed.provider
                for feed in self.feeds
            )
        )

    def summary(self) -> dict:
        return {
            "count": self.count,
            "connected": self.connected_count,
            "average_latency": round(
                self.average_latency,
                2,
            ),
            "total_updates": self.total_updates,
            "feed_distribution": self.feed_distribution,
            "provider_distribution": self.provider_distribution,
        }