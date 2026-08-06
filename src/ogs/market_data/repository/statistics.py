"""
OGS Smart Money AI

Repository Statistics
"""

from __future__ import annotations

from collections import Counter

from ogs.framework import BaseStatistics

from .collection import RepositoryCollection
from .domain import Repository


class RepositoryStatistics(BaseStatistics):
    """
    Computes repository statistics.
    """

    def __init__(
        self,
        repositories: RepositoryCollection,
    ) -> None:
        self.repositories = repositories

    @property
    def count(self) -> int:
        return len(self.repositories)

    @property
    def active_count(self) -> int:
        return len(self.repositories.active())

    @property
    def archived_count(self) -> int:
        return len(self.repositories.archived())

    @property
    def total_records(self) -> int:
        return self.repositories.total_records()

    @property
    def average_records(self) -> float:
        return self.repositories.average_records()

    @property
    def largest_repository(self) -> Repository | None:
        return self.repositories.largest()

    @property
    def smallest_repository(self) -> Repository | None:
        return self.repositories.smallest()

    @property
    def repository_distribution(self) -> dict[str, int]:
        return dict(
            Counter(
                repository.repository_type.value
                for repository in self.repositories
            )
        )

    def summary(self) -> dict:
        return {
            "count": self.count,
            "active": self.active_count,
            "archived": self.archived_count,
            "total_records": self.total_records,
            "average_records": self.average_records,
            "largest_repository": (
                self.largest_repository.name
                if self.largest_repository
                else None
            ),
            "smallest_repository": (
                self.smallest_repository.name
                if self.smallest_repository
                else None
            ),
            "repository_distribution": (
                self.repository_distribution
            ),
        }