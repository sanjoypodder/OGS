"""
Standard engine result contract for OGS Financial Operating System.

Project      : OGS-FOS
Module       : Base
Organization : Om Ganapati Solution
Version      : 0.0.1
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from types import MappingProxyType
from typing import Any, Generic, Mapping, TypeVar


T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class EngineResult(Generic[T]):
    """Immutable result returned by an OGS engine execution."""

    success: bool

    data: T | None = None

    error: str | None = None

    metadata: Mapping[str, Any] = field(
        default_factory=dict
    )

    completed_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def __post_init__(self) -> None:
        """Validate and normalize result state."""

        if self.completed_at.tzinfo is None:
            raise ValueError(
                "completed_at must be timezone-aware."
            )

        error = self.error.strip() if self.error else None

        if self.success and error is not None:
            raise ValueError(
                "A successful engine result cannot contain an error."
            )

        if not self.success and not error:
            raise ValueError(
                "A failed engine result must contain an error."
            )

        object.__setattr__(
            self,
            "error",
            error,
        )

        object.__setattr__(
            self,
            "metadata",
            MappingProxyType(dict(self.metadata)),
        )

    @classmethod
    def ok(
        cls,
        data: T | None = None,
        *,
        metadata: Mapping[str, Any] | None = None,
    ) -> "EngineResult[T]":
        """Create a successful engine result."""

        return cls(
            success=True,
            data=data,
            metadata=metadata or {},
        )

    @classmethod
    def fail(
        cls,
        error: str,
        *,
        metadata: Mapping[str, Any] | None = None,
    ) -> "EngineResult[T]":
        """Create a failed engine result."""

        if not isinstance(error, str):
            raise TypeError("error must be a string.")

        normalized_error = error.strip()

        if not normalized_error:
            raise ValueError(
                "error cannot be empty or whitespace."
            )

        return cls(
            success=False,
            error=normalized_error,
            metadata=metadata or {},
        )

