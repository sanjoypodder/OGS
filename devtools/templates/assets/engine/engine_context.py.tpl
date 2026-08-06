"""
Engine execution context for {{PROJECT_NAME}}.

Project      : {{PROJECT_SHORT_NAME}}
Module       : {{MODULE_NAME}}
Organization : {{ORGANIZATION}}
Version      : {{PROJECT_VERSION}}
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from types import MappingProxyType
from typing import Any, Mapping
from uuid import uuid4


@dataclass(frozen=True, slots=True)
class EngineContext:
    """Immutable context supplied to an OGS engine execution."""

    execution_id: str = field(
        default_factory=lambda: uuid4().hex
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    symbol: str | None = None

    timeframe: str | None = None

    metadata: Mapping[str, Any] = field(
        default_factory=dict
    )

    def __post_init__(self) -> None:
        """Normalize and validate context state."""

        execution_id = self.execution_id.strip()

        if not execution_id:
            raise ValueError("execution_id cannot be empty.")

        if self.created_at.tzinfo is None:
            raise ValueError(
                "created_at must be timezone-aware."
            )

        symbol = self.symbol.strip() if self.symbol else None
        timeframe = self.timeframe.strip() if self.timeframe else None

        object.__setattr__(
            self,
            "execution_id",
            execution_id,
        )

        object.__setattr__(
            self,
            "symbol",
            symbol or None,
        )

        object.__setattr__(
            self,
            "timeframe",
            timeframe or None,
        )

        object.__setattr__(
            self,
            "metadata",
            MappingProxyType(dict(self.metadata)),
        )
