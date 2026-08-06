"""
===========================================================

OGS Smart Money AI

Validation Statistics Tests

===========================================================
"""

from ogs.validation import ValidationStatistics


def test_statistics():

    stats = ValidationStatistics(
        valid=10,
        invalid=5,
    )

    assert stats.valid == 10
    assert stats.invalid == 5
    assert stats.total == 15