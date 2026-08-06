"""
Performance tests for TickAnalyzer.
"""

from datetime import UTC, datetime, timedelta

from ogs.market_data.tick import (
    ProviderType,
    Tick,
)
from ogs.market_data.tick.analyzer import TickAnalyzer
from ogs.market_data.tick.collection import TickCollection


def build_collection(size=1000):

    collection = TickCollection()

    now = datetime.now(UTC)

    for i in range(size):

        collection.append(

            Tick(
                symbol=f"EURUSD{i}",
                timestamp=now + timedelta(milliseconds=i),
                bid=float(i),
                ask=float(i) + 0.2,
                last=float(i) + 0.1,
                volume=1,
                provider=ProviderType.FYERS,
            )

        )

    return collection


def test_large_collection():

    analyzer = TickAnalyzer()

    collection = build_collection(1000)

    result = analyzer.analyze(collection)

    assert result["count"] == 1000


def test_latest_large():

    analyzer = TickAnalyzer()

    latest = analyzer.latest(
        build_collection(1000)
    )

    assert latest.symbol == "EURUSD999"


def test_find_large():

    analyzer = TickAnalyzer()

    tick = analyzer.find(
        build_collection(1000),
        "EURUSD999",
    )

    assert tick.symbol == "EURUSD999"


def test_provider_distribution_large():

    analyzer = TickAnalyzer()

    result = analyzer.provider_analysis(
        build_collection(1000)
    )

    assert result["FYERS"] == 1000


def test_multiple_analysis_runs():

    analyzer = TickAnalyzer()

    collection = build_collection(500)

    for _ in range(25):

        result = analyzer.analyze(collection)

        assert result["count"] == 500