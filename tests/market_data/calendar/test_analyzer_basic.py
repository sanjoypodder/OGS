"""
Tests for Calendar analyzer.
"""

from datetime import date

from ogs.market_data.calendar import (
    Calendar,
    CalendarAnalyzer,
    CalendarCollection,
    CalendarStatus,
    CalendarType,
)


def test_analyze():

    collection = CalendarCollection()

    collection.add(
        Calendar(
            calendar_id="1",
            exchange="NSE",
            market="Cash",
            trading_date=date.today(),
            calendar_type=CalendarType.TRADING_DAY,
            status=CalendarStatus.OPEN,
        )
    )

    analyzer = CalendarAnalyzer()

    result = analyzer.analyze(collection)

    assert isinstance(result, dict)

    assert "summary" in result
    assert "calendar_analysis" in result
    assert "distribution_analysis" in result