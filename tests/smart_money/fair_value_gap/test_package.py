"""
===========================================================

OGS Smart Money AI

Fair Value Gap Package Tests

===========================================================
"""

from ogs.smart_money.fair_value_gap import (
    FairValueGap,
    FairValueGapAnalyzer,
    FairValueGapDirection,
    FairValueGapSeries,
    FairValueGapStatistics,
    FairValueGapValidator,
)


def test_package():

    assert FairValueGap is not None
    assert FairValueGapDirection is not None
    assert FairValueGapSeries is not None
    assert FairValueGapValidator is not None
    assert FairValueGapStatistics is not None
    assert FairValueGapAnalyzer is not None