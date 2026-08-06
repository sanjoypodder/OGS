"""
Tests for Industry package exports.
"""

from ogs.market_data.industry import (
    __version__,
    Industry,
    IndustryAnalyzer,
    IndustryCollection,
    IndustryFactory,
    IndustryStatistics,
    IndustryStatus,
    IndustryType,
    IndustryValidator,
)


def test_version():

    assert __version__ == "0.1.0"


def test_exports():

    assert Industry is not None
    assert IndustryAnalyzer is not None
    assert IndustryCollection is not None
    assert IndustryFactory is not None
    assert IndustryStatistics is not None
    assert IndustryValidator is not None
    assert IndustryType is not None
    assert IndustryStatus is not None