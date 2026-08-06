"""
OGS Smart Money AI

Repository Analyzer
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import RepositoryCollection
from .statistics import RepositoryStatistics


class RepositoryAnalyzer(BaseAnalyzer):
    """
    Analyzer for Repository collections.
    """

    def __init__(
        self,
        repositories: RepositoryCollection,
    ) -> None:
        self.repositories = repositories
        self.statistics = RepositoryStatistics(
            repositories
        )

    # Required by BaseAnalyzer
    def analyze(self) -> dict:
        return self.repository_analysis()

    def summary(self) -> dict:
        return self.statistics.summary()

    def storage_analysis(self) -> dict:
        return {
            "repositories": self.statistics.count,
            "distribution": (
                self.statistics.repository_distribution
            ),
        }

    def capacity_analysis(self) -> dict:
        largest = self.statistics.largest_repository
        smallest = self.statistics.smallest_repository

        return {
            "total_records": (
                self.statistics.total_records
            ),
            "average_records": round(
                self.statistics.average_records,
                2,
            ),
            "largest_repository": (
                largest.name
                if largest
                else None
            ),
            "smallest_repository": (
                smallest.name
                if smallest
                else None
            ),
        }

    def provider_analysis(self) -> dict:
        providers = {}

        for repository in self.repositories:
            providers.setdefault(
                repository.provider,
                0,
            )
            providers[repository.provider] += 1

        return providers

    def repository_analysis(self) -> dict:
        return {
            "summary": self.summary(),
            "storage": (
                self.storage_analysis()
            ),
            "capacity": (
                self.capacity_analysis()
            ),
            "providers": (
                self.provider_analysis()
            ),
        }