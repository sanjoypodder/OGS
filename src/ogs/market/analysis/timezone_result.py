"""
===========================================================

OGS Smart Money AI

Timezone Normalization Result

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TimezoneResult:
    """
    Result of timezone normalization.
    """

    normalized: int
    skipped: int

    @property
    def total(self) -> int:
        return self.normalized + self.skipped