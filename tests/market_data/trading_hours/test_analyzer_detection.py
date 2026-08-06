"""
Tests for TradingHours analyzer detection.
"""

from ogs.market_data.trading_hours import (
    TradingHours,
    TradingHoursAnalyzer,
    TradingHoursCollection,
    TradingHoursStatus,
    TradingHoursType,
)


def test_distribution_detection():

    collection = TradingHoursCollection()

    collection.add(
        TradingHours(
            trading_hours_id="TH001",
            exchange="NSE",
            market="Equity",
            session_name="Regular",
            trading_hours_type=TradingHoursType.REGULAR,
            status=TradingHoursStatus.ACTIVE,
        )
    )

    collection.add(
        TradingHours(
            trading_hours_id="TH002",
            exchange="NYSE",
            market="Equity",
            session_name="Pre",
            trading_hours_type=TradingHoursType.PRE_MARKET,
            status=TradingHoursStatus.ACTIVE,
        )
    )

    analyzer = TradingHoursAnalyzer()

    result = analyzer.analyze(collection)

    distribution = result["distribution_analysis"]

    assert (
        distribution["trading_hours_type"]["REGULAR"]
        == 1
    )

    assert (
        distribution["trading_hours_type"]["PRE_MARKET"]
        == 1
    )