"""
===========================================================

OGS Smart Money AI

Swing Package Tests

===========================================================
"""

from ogs.smart_money.swing import (
    Swing,
    SwingAnalyzer,
    SwingSeries,
    SwingStatistics,
    SwingType,
    SwingValidator,
)


def test_package_exports():

    assert Swing is not None
    assert SwingType is not None
    assert SwingSeries is not None
    assert SwingAnalyzer is not None
    assert SwingValidator is not None
    assert SwingStatistics is not None