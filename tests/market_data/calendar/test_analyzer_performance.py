"""
Calendar analyzer performance tests.
"""

from datetime import date

from ogs.market_data.calendar import (
    Calendar,
    CalendarAnalyzer,
    CalendarCollection,
    CalendarStatus,
    CalendarType,
)


def test_large_collection():

    collection = CalendarCollection()

    for i in range(1000):

        collection.add(
            Calendar(
                calendar_id=str(i),
                exchange="NSE",
                market="Cash",
                trading_date=date.today(),
                calendar_type=CalendarType.TRADING_DAY,
                status=CalendarStatus.OPEN,
            )
        )

    analyzer = CalendarAnalyzer()

    result = analyzer.analyze(collection)

    assert (
        result["summary"]["count"]
        == 1000
    )

    assert (
        result["calendar_analysis"]["trading_days"]
        == 1000
    )

    assert (
        result["calendar_analysis"]["open_days"]
        == 1000
    )