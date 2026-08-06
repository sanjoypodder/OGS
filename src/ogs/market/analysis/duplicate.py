"""
===========================================================

OGS Smart Money AI

Duplicate Candle Domain Object

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Duplicate:
    """
    Represents a duplicate candle.
    """

    index: int

    timestamp: datetime

    def __str__(self) -> str:
        return (
            f"Duplicate(index={self.index}, "
            f"timestamp={self.timestamp.isoformat()})"
        )