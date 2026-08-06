"""
OGS Smart Money AI

Repository Collection
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator

from ogs.framework import BaseCollection

from .domain import Repository
from .enums import RepositoryStatus


class RepositoryCollection(BaseCollection):
    """
    Collection of Repository objects.
    """

    def __init__(
        self,
        repositories: Iterable[Repository] = (),
    ) -> None:
        self._repositories = list(repositories)

    def __iter__(self) -> Iterator[Repository]:
        return iter(self._repositories)

    def __len__(self) -> int:
        return len(self._repositories)

    def __getitem__(self, index: int) -> Repository:
        return self._repositories[index]

    def add(self, repository: Repository) -> None:
        self._repositories.append(repository)

    def active(self) -> "RepositoryCollection":
        return RepositoryCollection(
            r
            for r in self._repositories
            if r.status == RepositoryStatus.ACTIVE
        )

    def archived(self) -> "RepositoryCollection":
        return RepositoryCollection(
            r
            for r in self._repositories
            if r.status == RepositoryStatus.ARCHIVED
        )

    def read_only(self) -> "RepositoryCollection":
        return RepositoryCollection(
            r
            for r in self._repositories
            if r.read_only
        )

    def by_provider(
        self,
        provider: str,
    ) -> "RepositoryCollection":
        provider = provider.casefold()

        return RepositoryCollection(
            r
            for r in self._repositories
            if r.provider.casefold() == provider
        )

    def by_symbol(
        self,
        symbol: str,
    ) -> "RepositoryCollection":
        symbol = symbol.casefold()

        return RepositoryCollection(
            r
            for r in self._repositories
            if r.symbol.casefold() == symbol
        )

    def by_timeframe(
        self,
        timeframe: str,
    ) -> "RepositoryCollection":
        timeframe = timeframe.casefold()

        return RepositoryCollection(
            r
            for r in self._repositories
            if r.timeframe.casefold() == timeframe
        )

    def find(
        self,
        name: str,
    ) -> Repository | None:
        name = name.casefold()

        for repository in self._repositories:
            if repository.name.casefold() == name:
                return repository

        return None

    def largest(self) -> Repository | None:
        if not self._repositories:
            return None

        return max(
            self._repositories,
            key=lambda r: r.records,
        )

    def smallest(self) -> Repository | None:
        if not self._repositories:
            return None

        return min(
            self._repositories,
            key=lambda r: r.records,
        )

    def total_records(self) -> int:
        return sum(
            repository.records
            for repository in self._repositories
        )

    def average_records(self) -> float:
        if not self._repositories:
            return 0.0

        return (
            self.total_records()
            / len(self._repositories)
        )

    def to_list(self) -> list[Repository]:
        return list(self._repositories)