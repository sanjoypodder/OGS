"""
===========================================================

OGS Smart Money AI

Validation Enums

===========================================================
"""

from __future__ import annotations

from enum import StrEnum


class ValidationStatus(StrEnum):
    """
    Validation lifecycle.
    """

    VALID = "VALID"
    INVALID = "INVALID"