"""
Edge case tests for ProviderAnalyzer.
"""

from ogs.market_data.provider import (
    ProviderAnalyzer,
    ProviderCollection,
)


def test_empty_collection() -> None:
    analyzer = ProviderAnalyzer(
        ProviderCollection()
    )

    summary = analyzer.summary()

    assert summary["count"] == 0


def test_empty_connection_analysis() -> None:
    analyzer = ProviderAnalyzer(
        ProviderCollection()
    )

    report = analyzer.connection_analysis()

    assert report["total"] == 0
    assert report["availability_percent"] == 0.0


def test_empty_latency_analysis() -> None:
    analyzer = ProviderAnalyzer(
        ProviderCollection()
    )

    report = analyzer.latency_analysis()

    assert report["fastest_provider"] is None
    assert report["slowest_provider"] is None


def test_empty_capability_analysis() -> None:
    analyzer = ProviderAnalyzer(
        ProviderCollection()
    )

    report = analyzer.capability_analysis()

    assert report["live_capable"] == 0
    assert report["historical_capable"] == 0
    assert report["websocket_capable"] == 0