"""
Tests for Screener analyzer performance.
"""

from ogs.market_data.screener import (
    Screener,
    ScreenerAnalyzer,
    ScreenerCollection,
    ScreenerStatus,
    ScreenerType,
)


def test_large_collection():

    collection = ScreenerCollection()

    for i in range(1000):

        collection.add(
            Screener(
                screener_id=f"SCR{i}",
                screener_name=f"Screener {i}",
                screener_type=(
                    ScreenerType.SMART_MONEY
                ),
                status=ScreenerStatus.ACTIVE,
                filters=[
                    {"field": "volume"},
                    {"field": "trend"},
                ],
            )
        )

    analyzer = ScreenerAnalyzer()

    result = analyzer.analyze(collection)

    assert (
        result["summary"]["count"]
        == 1000
    )

    assert (
        result["screener_analysis"][
            "total_screeners"
        ]
        == 1000
    )

    assert (
        result["screener_analysis"][
            "active_screeners"
        ]
        == 1000
    )

    assert (
        result["screener_analysis"][
            "total_filters"
        ]
        == 2000
    )