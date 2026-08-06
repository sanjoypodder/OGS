"""
Tests for Calendar package exports.
"""

from ogs.market_data.calendar import (
    __version__,
    Calendar,
    CalendarAnalyzer,
    CalendarCollection,
    CalendarFactory,
    CalendarStatistics,
    CalendarStatus,
    CalendarType,
    CalendarValidator,
)


def test_version():

    assert __version__ == "0.1.0"


def test_exports():

    assert Calendar is not None
    assert CalendarAnalyzer is not None
    assert CalendarCollection is not None
    assert CalendarFactory is not None
    assert CalendarStatistics is not None
    assert CalendarValidator is not None
    assert CalendarType is not None
    assert CalendarStatus is not None