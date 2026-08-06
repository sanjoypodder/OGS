"""
Calendar analyzer edge cases.
"""

from ogs.market_data.calendar import (
    CalendarAnalyzer,
    CalendarCollection,
)


def test_empty_collection():

    analyzer = CalendarAnalyzer()

    result = analyzer.analyze(
        CalendarCollection()
    )

    assert result["summary"]["count"] == 0


def test_empty_distribution():

    analyzer = CalendarAnalyzer()

    result = analyzer.analyze(
        CalendarCollection()
    )

    distribution = result[
        "distribution_analysis"
    ]["calendar_type"]

    assert isinstance(distribution, dict)