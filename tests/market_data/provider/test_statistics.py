"""
Tests for ProviderStatistics.
"""

from ogs.market_data.provider import (
    ConnectionStatus,
    ProviderCollection,
    ProviderFactory,
    ProviderStatistics,
    ProviderType,
)


def create_statistics() -> ProviderStatistics:
    collection = ProviderCollection(
        [
            ProviderFactory.create(
                name="FYERS",
                provider_type=ProviderType.BROKER,
                status=ConnectionStatus.CONNECTED,
                latency_ms=10,
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

    return ProviderStatistics(collection)


def test_counts() -> None:
    stats = create_statistics()

    assert stats.count == 3
    assert stats.connected_count == 2
    assert stats.offline_count == 1


def test_average_latency() -> None:
    stats = create_statistics()

    assert stats.average_latency == (10 + 5 + 50) / 3


def test_fastest_provider() -> None:
    stats = create_statistics()

    assert stats.fastest_provider.name == "NSE"


def test_slowest_provider() -> None:
    stats = create_statistics()

    assert stats.slowest_provider.name == "CSV"


def test_capabilities() -> None:
    stats = create_statistics()

    assert stats.live_capable == 2
    assert stats.historical_capable == 3
    assert stats.websocket_capable == 1


def test_distribution() -> None:
    stats = create_statistics()

    distribution = stats.provider_distribution

    assert distribution["BROKER"] == 1
    assert distribution["EXCHANGE"] == 1
    assert distribution["CSV"] == 1


def test_summary() -> None:
    stats = create_statistics()

    summary = stats.summary()

    assert summary["count"] == 3
    assert summary["connected"] == 2
    assert summary["offline"] == 1
    assert summary["fastest_provider"] == "NSE"
    assert summary["slowest_provider"] == "CSV"