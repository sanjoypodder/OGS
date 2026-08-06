"""
===========================================================

OGS Smart Money AI

CHOCH Package Tests

===========================================================
"""

from ogs.smart_money.choch import (
    CHOCH,
    CHOCHAnalyzer,
    CHOCHSeries,
    CHOCHStatistics,
    CHOCHType,
    CHOCHValidator,
)


def test_package_exports():

    assert CHOCH is not None
    assert CHOCHType is not None
    assert CHOCHSeries is not None
    assert CHOCHAnalyzer is not None
    assert CHOCHValidator is not None
    assert CHOCHStatistics is not None