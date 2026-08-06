"""
OGS Smart Money AI

Feed Analyzer
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import FeedCollection
from .statistics import FeedStatistics


class FeedAnalyzer(BaseAnalyzer):
    """
    Analyzer for Feed collections.
    """

    def __init__(
        self,
        feeds: FeedCollection,
    ):
        self.feeds = feeds
        self.statistics = FeedStatistics(
            feeds
        )

    def analyze(self) -> dict:
        return self.feed_analysis()

    def summary(self) -> dict:
        return self.statistics.summary()

    def latency_analysis(self) -> dict:
        return {
            "average_latency":
                round(
                    self.statistics.average_latency,
                    2,
                ),
            "fastest_feed":
                (
                    self.statistics.fastest_feed.name
                    if self.statistics.fastest_feed
                    else None
                ),
            "slowest_feed":
                (
                    self.statistics.slowest_feed.name
                    if self.statistics.slowest_feed
                    else None
                ),
        }

    def connection_analysis(self) -> dict:
        return {
            "connected":
                self.statistics.connected_count,
            "total":
                self.statistics.count,
        }

    def performance_analysis(self) -> dict:
        return {
            "feed_distribution":
                self.statistics.feed_distribution,
            "provider_distribution":
                self.statistics.provider_distribution,
            "total_updates":
                self.statistics.total_updates,
        }

    def feed_analysis(self) -> dict:
        return {
            "summary":
                self.summary(),
            "latency":
                self.latency_analysis(),
            "connection":
                self.connection_analysis(),
            "performance":
                self.performance_analysis(),
        }