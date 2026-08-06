"""
BOS Package Tests
"""

from ogs.smart_money.bos import (
    BOS,
    BOSAnalyzer,
    BOSSeries,
    BOSStatistics,
    BOSType,
    BOSValidator,
)


def test_package_exports():

    assert BOS is not None
    assert BOSAnalyzer is not None
    assert BOSSeries is not None
    assert BOSValidator is not None
    assert BOSStatistics is not None
    assert BOSType is not None