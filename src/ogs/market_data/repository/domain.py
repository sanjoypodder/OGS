"""
OGS Smart Money AI

Repository Domain
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime

from .enums import (
    RepositoryStatus,
    RepositoryType,
)


@dataclass(slots=True, frozen=True)
class Repository:
    """
    Represents a market data repository.

    A repository stores market data for a specific
    provider, symbol, and timeframe regardless of
    the underlying storage implementation.
    """

    name: str

    provider: str = ""

    symbol: str = ""

    timeframe: str = ""

    repository_type: RepositoryType = RepositoryType.UNKNOWN

    status: RepositoryStatus = RepositoryStatus.UNKNOWN

    records: int = 0

    from dataclasses import dataclass, field

    last_updated: datetime = field(
            default_factory=lambda: datetime.now(UTC)
        )

    readable: bool = True

    writable: bool = True

    @property
    def active(self) -> bool:
        """
        Returns True if repository is active.
        """
        return self.status == RepositoryStatus.ACTIVE

    @property
    def archived(self) -> bool:
        """
        Returns True if repository is archived.
        """
        return self.status == RepositoryStatus.ARCHIVED

    @property
    def read_only(self) -> bool:
        """
        Returns True if repository is read-only.
        """
        return self.status == RepositoryStatus.READ_ONLY

    @property
    def is_valid(self) -> bool:
        """
        Lightweight validation.
        """
        return (
            bool(self.name.strip())
            and isinstance(
                self.repository_type,
                RepositoryType,
            )
            and isinstance(
                self.status,
                RepositoryStatus,
            )
            and self.records >= 0
        )

    def to_dict(self) -> dict:
        """
        Convert Repository to dictionary.
        """

        return {
            "name": self.name,
            "provider": self.provider,
            "symbol": self.symbol,
            "timeframe": self.timeframe,
            "repository_type": self.repository_type.value,
            "status": self.status.value,
            "records": self.records,
            "last_updated": (
                self.last_updated.isoformat()
            ),
            "readable": self.readable,
            "writable": self.writable,
        }

    def __str__(self) -> str:
        return (
            f"{self.name} "
            f"[{self.repository_type.value}] "
            f"{self.records:,} records"
        )

    def __repr__(self) -> str:
        return (
            "Repository("
            f"name='{self.name}', "
            f"type={self.repository_type.value}, "
            f"records={self.records})"
        )