"""
===========================================================

OGS Smart Money AI

Validation Enums Tests

===========================================================
"""

from ogs.validation import ValidationStatus


def test_values():

    assert ValidationStatus.VALID == "VALID"
    assert ValidationStatus.INVALID == "INVALID"


def test_count():

    assert len(ValidationStatus) == 2