"""
Tests for Timeframe package.
"""

from ogs.market_data.timeframe import (
    Timeframe,
    TimeframeAnalyzer,
    TimeframeCollection,
    TimeframeFactory,
    TimeframeStatistics,
    TimeframeType,
    TimeframeValidator,
)


def test_package_imports():

    assert Timeframe is not None
    assert TimeframeAnalyzer is not None
    assert TimeframeCollection is not None
    assert TimeframeFactory is not None
    assert TimeframeStatistics is not None
    assert TimeframeType is not None
    assert TimeframeValidator is not None