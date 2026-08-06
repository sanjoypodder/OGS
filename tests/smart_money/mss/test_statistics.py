"""
===========================================================

OGS Smart Money AI

MSS Statistics Tests

===========================================================
"""

from ogs.smart_money.mss import MSSStatistics


def test_statistics_creation():

    stats = MSSStatistics()

    assert stats is not None