"""
Tests for Screener analyzer distribution.
"""

from ogs.market_data.screener import (
    Screener,
    ScreenerAnalyzer,
    ScreenerCollection,
    ScreenerStatus,
    ScreenerType,
)


def test_distribution_detection():

    collection = ScreenerCollection()

    collection.add(
        Screener(
            screener_id="SCR001",
            screener_name="SMC",
            screener_type=(
                ScreenerType.SMART_MONEY
            ),
            status=ScreenerStatus.ACTIVE,
        )
    )

    collection.add(
        Screener(
            screener_id="SCR002",
            screener_name="AI",
            screener_type=ScreenerType.AI,
            status=ScreenerStatus.ACTIVE,
        )
    )

    analyzer = ScreenerAnalyzer()

    result = analyzer.analyze(collection)

    distribution = result[
        "distribution_analysis"
    ]

    assert (
        distribution["screener_type"][
            "SMART_MONEY"
        ]
        == 1
    )

    assert (
        distribution["screener_type"]["AI"]
        == 1
    )