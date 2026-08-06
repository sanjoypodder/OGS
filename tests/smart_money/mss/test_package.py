"""
===========================================================

OGS Smart Money AI

MSS Package Tests

===========================================================
"""

from ogs.smart_money.mss import (
    MSS,
    MSSAnalyzer,
    MSSSeries,
    MSSStatistics,
    MSSType,
    MSSValidator,
)


def test_package_exports():

    assert MSS is not None
    assert MSSType is not None
    assert MSSSeries is not None
    assert MSSAnalyzer is not None
    assert MSSValidator is not None
    assert MSSStatistics is not None