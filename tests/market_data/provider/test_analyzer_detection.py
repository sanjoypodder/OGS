"""
Tests for ProviderAnalyzer detection methods.
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
                name="Broker",
                provider_type=ProviderType.BROKER,
                status=ConnectionStatus.CONNECTED,
                latency_ms=12,
                supports_live=True,
                supports_websocket=True,
            ),
            ProviderFactory.create(
                name="Exchange",
                provider_type=ProviderType.EXCHANGE,
                status=ConnectionStatus.DISCONNECTED,
                latency_ms=30,
            ),
        ]
    )

    return ProviderAnalyzer(collection)


def test_connection_analysis() -> None:
    analyzer = create_analyzer()

    report = analyzer.connection_analysis()

    assert report["total"] == 2
    assert report["connected"] == 1
    assert report["offline"] == 1
    assert report["availability_percent"] == 50.0


def test_latency_analysis() -> None:
    analyzer = create_analyzer()

    report = analyzer.latency_analysis()

    assert report["fastest_provider"] == "Broker"
    assert report["slowest_provider"] == "Exchange"


def test_capability_analysis() -> None:
    analyzer = create_analyzer()

    report = analyzer.capability_analysis()

    assert report["live_capable"] == 1
    assert report["websocket_capable"] == 1