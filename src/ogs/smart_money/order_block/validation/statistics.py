"""
===========================================================

OGS Smart Money AI

Order Block Validation Statistics

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class OrderBlockValidationStatistics:

    validated: int = 0

    rejected: int = 0

    @property
    def total(self):

        return self.validated + self.rejected