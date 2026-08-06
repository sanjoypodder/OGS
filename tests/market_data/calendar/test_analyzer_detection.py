"""
Calendar analyzer distribution tests.
"""

from datetime import date

from ogs.market_data.calendar import (
    Calendar,
    CalendarAnalyzer,
    CalendarCollection,
    CalendarStatus,
    CalendarType,
)


def test_distribution_detection():

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

    collection.add(
        Calendar(
            calendar_id="2",
            exchange="NSE",
            market="Cash",
            trading_date=date.today(),
            calendar_type=CalendarType.HOLIDAY,
            status=CalendarStatus.CLOSED,
        )
    )

    analyzer = CalendarAnalyzer()

    result = analyzer.analyze(collection)

    distribution = result["distribution_analysis"]

    assert distribution["calendar_type"]["TRADING_DAY"] == 1
    assert distribution["calendar_type"]["HOLIDAY"] == 1