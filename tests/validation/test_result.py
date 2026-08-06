"""
===========================================================

OGS Smart Money AI

Validation Result Tests

===========================================================
"""

from dataclasses import FrozenInstanceError

import pytest

from ogs.validation import (
    ValidationResult,
    ValidationStatus,
)


def test_valid():

    result = ValidationResult(
        status=ValidationStatus.VALID,
    )

    assert result.is_valid
    assert not result.is_invalid


def test_invalid():

    result = ValidationResult(
        status=ValidationStatus.INVALID,
        reason="Weak displacement",
    )

    assert result.is_invalid
    assert not result.is_valid


def test_reason():

    result = ValidationResult(
        status=ValidationStatus.INVALID,
        reason="Invalid OB",
    )

    assert result.reason == "Invalid OB"


def test_frozen():

    result = ValidationResult(
        status=ValidationStatus.VALID,
    )

    with pytest.raises(FrozenInstanceError):
        result.status = ValidationStatus.INVALID