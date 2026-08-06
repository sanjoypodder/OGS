"""
Performance tests for ProviderAnalyzer.
"""

from time import perf_counter

from ogs.market_data.provider import (
    ConnectionStatus,
    ProviderAnalyzer,
    ProviderCollection,
    ProviderFactory,
    ProviderType,
)


def test_large_collection_performance() -> None:
    providers = []

    for index in range(1000):
        providers.append(
            ProviderFactory.create(
                name=f"Provider-{index}",
                provider_type=ProviderType.BROKER,
                status=ConnectionStatus.CONNECTED,
                latency_ms=index % 100,
                supports_live=True,
                supports_historical=True,
            )
        )

    analyzer = ProviderAnalyzer(
        ProviderCollection(providers)
    )

    start = perf_counter()

    report = analyzer.provider_analysis()

    elapsed = perf_counter() - start

    assert report["summary"]["count"] == 1000

    # Should comfortably execute well under 1 second.
    assert elapsed < 1.0