"""
===========================================================

OGS Smart Money AI

Universe Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from .enums import (
    UniverseStatus,
    UniverseType,
)


@dataclass(slots=True)
class Universe:
    """
    Trading Universe.
    """

    universe_id: str = ""

    universe_name: str = ""

    description: str = ""

    market: str = ""

    owner: str = ""

    symbols: list[str] = field(
        default_factory=list
    )

    source: str = ""

    universe_type: UniverseType = (
        UniverseType.UNKNOWN
    )

    status: UniverseStatus = (
        UniverseStatus.UNKNOWN
    )

    active: bool = True

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def is_active(self) -> bool:

        return (
            self.active
            and self.status == UniverseStatus.ACTIVE
        )

    @property
    def is_valid(self) -> bool:

        return (
            bool(self.universe_id.strip())
            and bool(self.universe_name.strip())
        )

    @property
    def symbol_count(self) -> int:

        return len(self.symbols)

    def add_symbol(
        self,
        symbol: str,
    ) -> None:

        if symbol not in self.symbols:
            self.symbols.append(symbol)

    def remove_symbol(
        self,
        symbol: str,
    ) -> None:

        if symbol in self.symbols:
            self.symbols.remove(symbol)

    def to_dict(self) -> dict:

        return {
            "universe_id": self.universe_id,
            "universe_name": self.universe_name,
            "description": self.description,
            "market": self.market,
            "owner": self.owner,
            "symbols": list(self.symbols),
            "source": self.source,
            "universe_type": self.universe_type.value,
            "status": self.status.value,
            "active": self.active,
        }

    def __str__(self) -> str:

        return (
            f"Universe("
            f"id='{self.universe_id}', "
            f"name='{self.universe_name}')"
        )