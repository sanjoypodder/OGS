"""
OGS Smart Money AI

Repository Validator
"""

from __future__ import annotations

from datetime import datetime

from ogs.framework import BaseValidator

from .domain import Repository
from .enums import (
    RepositoryStatus,
    RepositoryType,
)


class RepositoryValidator(BaseValidator):
    """
    Validator for Repository objects.
    """

    MIN_RECORDS = 0

    def validate(self, repository: Repository) -> None:
        """
        Validate a Repository instance.
        """

        if not isinstance(repository, Repository):
            raise TypeError(
                "repository must be a Repository instance."
            )

        if not isinstance(repository.name, str):
            raise TypeError(
                "name must be a string."
            )

        if not repository.name.strip():
            raise ValueError(
                "name cannot be empty."
            )

        if not isinstance(
            repository.provider,
            str,
        ):
            raise TypeError(
                "provider must be a string."
            )

        if not isinstance(
            repository.symbol,
            str,
        ):
            raise TypeError(
                "symbol must be a string."
            )

        if not isinstance(
            repository.timeframe,
            str,
        ):
            raise TypeError(
                "timeframe must be a string."
            )

        if not isinstance(
            repository.repository_type,
            RepositoryType,
        ):
            raise TypeError(
                "repository_type must be RepositoryType."
            )

        if not isinstance(
            repository.status,
            RepositoryStatus,
        ):
            raise TypeError(
                "status must be RepositoryStatus."
            )

        if not isinstance(
            repository.records,
            int,
        ):
            raise TypeError(
                "records must be int."
            )

        if repository.records < self.MIN_RECORDS:
            raise ValueError(
                "records cannot be negative."
            )

        if not isinstance(
            repository.last_updated,
            datetime,
        ):
            raise TypeError(
                "last_updated must be datetime."
            )

        if not isinstance(
            repository.readable,
            bool,
        ):
            raise TypeError(
                "readable must be bool."
            )

        if not isinstance(
            repository.writable,
            bool,
        ):
            raise TypeError(
                "writable must be bool."
            )

    def __call__(
        self,
        repository: Repository,
    ) -> Repository:
        """
        Validate and return Repository.
        """

        self.validate(repository)

        return repository