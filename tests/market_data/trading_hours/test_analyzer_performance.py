"""
Tests for TradingHours analyzer performance.
"""

from ogs.market_data.trading_hours import (
    TradingHours,
    TradingHoursAnalyzer,
    TradingHoursCollection,
    TradingHoursStatus,
    TradingHoursType,
)


def test_large_collection():

    collection = TradingHoursCollection()

    for i in range(1000):

        collection.add(
            TradingHours(
                trading_hours_id=f"TH{i}",
                exchange="NSE",
                market="Equity",
                session_name="Regular",
                trading_hours_type=TradingHoursType.REGULAR,
                status=TradingHoursStatus.ACTIVE,
            )
        )

    analyzer = TradingHoursAnalyzer()

    result = analyzer.analyze(collection)

    assert (
        result["summary"]["count"]
        == 1000
    )

    assert (
        result["trading_hours_analysis"][
            "total_trading_hours"
        ]
        == 1000
    )

    assert (
        result["trading_hours_analysis"][
            "active_trading_hours"
        ]
        == 1000
    )

    assert (
        result["trading_hours_analysis"][
            "exchange_distribution"
        ]["NSE"]
        == 1000
    )