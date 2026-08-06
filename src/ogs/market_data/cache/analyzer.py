"""
OGS Smart Money AI

Cache Analyzer
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import CacheCollection
from .statistics import CacheStatistics


class CacheAnalyzer(BaseAnalyzer):
    """
    Analyzer for Cache collections.
    """

    def __init__(
        self,
        caches: CacheCollection,
    ):
        self.caches = caches
        self.statistics = CacheStatistics(
            caches
        )

    # Required by BaseAnalyzer
    def analyze(self) -> dict:
        return self.cache_analysis()

    def summary(self) -> dict:
        return self.statistics.summary()

    def capacity_analysis(self) -> dict:

        return {
            "total_capacity":
                self.statistics.total_capacity,
            "total_used":
                self.statistics.total_used,
            "largest_cache":
                (
                    self.statistics
                    .largest_cache.name
                    if self.statistics.largest_cache
                    else None
                ),
            "smallest_cache":
                (
                    self.statistics
                    .smallest_cache.name
                    if self.statistics.smallest_cache
                    else None
                ),
        }

    def utilization_analysis(self) -> dict:

        return {
            "utilization":
                round(
                    self.statistics
                    .utilization_percentage,
                    2,
                ),
            "hit_rate":
                round(
                    self.statistics.hit_rate,
                    2,
                ),
            "miss_rate":
                round(
                    self.statistics.miss_rate,
                    2,
                ),
        }

    def performance_analysis(self) -> dict:

        return {
            "distribution":
                self.statistics.cache_distribution,
            "active":
                self.statistics.active_count,
        }

    def cache_analysis(self) -> dict:

        return {
            "summary":
                self.summary(),
            "capacity":
                self.capacity_analysis(),
            "utilization":
                self.utilization_analysis(),
            "performance":
                self.performance_analysis(),
        }