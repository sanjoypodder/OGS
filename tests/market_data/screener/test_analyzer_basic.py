"""
Tests for Screener analyzer.
"""

from ogs.market_data.screener import (
    Screener,
    ScreenerAnalyzer,
    ScreenerCollection,
    ScreenerStatus,
    ScreenerType,
)


def test_analyze():

    collection = ScreenerCollection()

    collection.add(
        Screener(
            screener_id="SCR001",
            screener_name="SMC",
            screener_type=(
                ScreenerType.SMART_MONEY
            ),
            status=ScreenerStatus.ACTIVE,
            filters=[
                {"field": "volume"},
            ],
        )
    )

    analyzer = ScreenerAnalyzer()

    result = analyzer.analyze(collection)

    assert isinstance(result, dict)

    assert "summary" in result
    assert "screener_analysis" in result
    assert "distribution_analysis" in result