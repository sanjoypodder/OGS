"""
Tests for TradingHours analyzer.
"""

from ogs.market_data.trading_hours import (
    TradingHours,
    TradingHoursAnalyzer,
    TradingHoursCollection,
    TradingHoursStatus,
    TradingHoursType,
)


def test_analyze():

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

    analyzer = TradingHoursAnalyzer()

    result = analyzer.analyze(collection)

    assert isinstance(result, dict)

    assert "summary" in result
    assert "trading_hours_analysis" in result
    assert "distribution_analysis" in result