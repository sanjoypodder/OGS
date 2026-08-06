"""
Tests for ProviderAnalyzer basic functionality.
"""

from ogs.market_data.provider import (
    ConnectionStatus,
    ProviderAnalyzer,
    ProviderCollection,
    ProviderFactory,
    ProviderType,
)


def create_analyzer() -> ProviderAnalyzer:
    collection = ProviderCollection(
        [
            ProviderFactory.create(
                name="FYERS",
                provider_type=ProviderType.BROKER,
                status=ConnectionStatus.CONNECTED,
                latency_ms=15,
                supports_live=True,
                supports_historical=True,
                supports_websocket=True,
            ),
            ProviderFactory.create(
                name="NSE",
                provider_type=ProviderType.EXCHANGE,
                status=ConnectionStatus.CONNECTED,
                latency_ms=5,
                supports_live=True,
                supports_historical=True,
            ),
            ProviderFactory.create(
                name="CSV",
                provider_type=ProviderType.CSV,
                status=ConnectionStatus.DISCONNECTED,
                latency_ms=50,
                supports_historical=True,
            ),
        ]
    )

    return ProviderAnalyzer(collection)


def test_summary() -> None:
    analyzer = create_analyzer()

    summary = analyzer.summary()

    assert summary["count"] == 3
    assert summary["connected"] == 2
    assert summary["offline"] == 1


def test_provider_analysis() -> None:
    analyzer = create_analyzer()

    report = analyzer.provider_analysis()

    assert "summary" in report
    assert "connection" in report
    assert "latency" in report
    assert "capabilities" in report