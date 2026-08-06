"""
OGS Smart Money AI

Repository Factory
"""

from __future__ import annotations

from datetime import UTC, datetime

from ogs.framework import BaseFactory

from .domain import Repository
from .enums import (
    RepositoryStatus,
    RepositoryType,
)
from .validator import RepositoryValidator


class RepositoryFactory(BaseFactory):
    """
    Factory for Repository objects.
    """

    _validator = RepositoryValidator()

    @classmethod
    def create(
        cls,
        *,
        name: str,
        provider: str = "",
        symbol: str = "",
        timeframe: str = "",
        repository_type: RepositoryType = RepositoryType.UNKNOWN,
        status: RepositoryStatus = RepositoryStatus.UNKNOWN,
        records: int = 0,
        last_updated: datetime | None = None,
        readable: bool = True,
        writable: bool = True,
    ) -> Repository:
        """
        Create and validate Repository.
        """

        repository = Repository(
            name=name,
            provider=provider,
            symbol=symbol,
            timeframe=timeframe,
            repository_type=repository_type,
            status=status,
            records=records,
            last_updated=(
                last_updated
                if last_updated is not None
                else datetime.now(UTC)
            ),
            readable=readable,
            writable=writable,
        )

        return cls._validator(repository)

    @classmethod
    def memory(
        cls,
        name: str,
    ) -> Repository:
        """
        Create an in-memory repository.
        """

        return cls.create(
            name=name,
            repository_type=RepositoryType.IN_MEMORY,
            status=RepositoryStatus.ACTIVE,
        )

    @classmethod
    def database(
        cls,
        name: str,
    ) -> Repository:
        """
        Create a database repository.
        """

        return cls.create(
            name=name,
            repository_type=RepositoryType.DATABASE,
            status=RepositoryStatus.ACTIVE,
        )

    @classmethod
    def archive(
        cls,
        name: str,
    ) -> Repository:
        """
        Create an archived repository.
        """

        return cls.create(
            name=name,
            status=RepositoryStatus.ARCHIVED,
            writable=False,
        )

    @classmethod
    def clone(
        cls,
        repository: Repository,
    ) -> Repository:
        """
        Clone a Repository.
        """

        return cls.create(
            name=repository.name,
            provider=repository.provider,
            symbol=repository.symbol,
            timeframe=repository.timeframe,
            repository_type=repository.repository_type,
            status=repository.status,
            records=repository.records,
            last_updated=repository.last_updated,
            readable=repository.readable,
            writable=repository.writable,
        )