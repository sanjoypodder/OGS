"""
===========================================================

OGS Smart Money AI

CHOCH Statistics Tests

===========================================================
"""

from ogs.smart_money.choch import CHOCHStatistics


def test_statistics_creation():

    stats = CHOCHStatistics()

    assert stats is not None