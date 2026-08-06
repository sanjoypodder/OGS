"""
===========================================================

OGS Smart Money AI

Validation Result

===========================================================
"""

from __future__ import annotations

from dataclasses import dataclass

from .enums import ValidationStatus


@dataclass(frozen=True, slots=True)
class ValidationResult:
    """
    Generic validation result.
    """

    status: ValidationStatus

    reason: str | None = None

    @property
    def is_valid(self) -> bool:

        return self.status == ValidationStatus.VALID

    @property
    def is_invalid(self) -> bool:

        return not self.is_valid