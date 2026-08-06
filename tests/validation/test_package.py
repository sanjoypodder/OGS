"""
===========================================================

OGS Smart Money AI

Validation Package Tests

===========================================================
"""

from ogs.validation import (
    ValidationResult,
    ValidationStatistics,
    ValidationStatus,
    Validator,
)


def test_exports():

    assert ValidationStatus is not None
    assert ValidationResult is not None
    assert ValidationStatistics is not None
    assert Validator is not None