"""
===========================================================

OGS Smart Money AI

Validation Statistics

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ValidationStatistics:

    valid: int = 0

    invalid: int = 0

    @property
    def total(self):

        return self.valid + self.invalid