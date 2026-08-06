"""
===========================================================

OGS Smart Money AI

Watchlist Domain

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


from .enums import (
    WatchlistStatus,
    WatchlistType,
)


@dataclass(slots=True)
class Watchlist:
    """
    Market Watchlist.
    """

    watchlist_id: str = ""

    watchlist_name: str = ""

    description: str = ""

    market: str = ""

    owner: str = ""

    symbols: list[str] = field(
        default_factory=list
    )

    watchlist_type: WatchlistType = (
        WatchlistType.UNKNOWN
    )

    status: WatchlistStatus = (
        WatchlistStatus.UNKNOWN
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
            and self.status == WatchlistStatus.ACTIVE
        )

    @property
    def is_valid(self) -> bool:

        return (
            bool(self.watchlist_id.strip())
            and bool(self.watchlist_name.strip())
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
            "watchlist_id": self.watchlist_id,
            "watchlist_name": self.watchlist_name,
            "description": self.description,
            "market": self.market,
            "owner": self.owner,
            "symbols": list(self.symbols),
            "watchlist_type": self.watchlist_type.value,
            "status": self.status.value,
            "active": self.active,
        }

    def __str__(self) -> str:

        return (
            f"Watchlist("
            f"id='{self.watchlist_id}', "
            f"name='{self.watchlist_name}')"
        )