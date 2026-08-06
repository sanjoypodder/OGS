"""
Edge case tests for TickAnalyzer.
"""

from datetime import UTC, datetime

from ogs.market_data.tick import (
    ProviderType,
    Tick,
)
from ogs.market_data.tick.analyzer import TickAnalyzer
from ogs.market_data.tick.collection import TickCollection


def test_empty_collection():

    analyzer = TickAnalyzer()

    collection = TickCollection()

    result = analyzer.analyze(collection)

    assert result["count"] == 0
    assert result["total_volume"] == 0
    assert result["buy_ticks"] == 0
    assert result["sell_ticks"] == 0


def test_latest_empty():

    analyzer = TickAnalyzer()

    assert analyzer.latest(TickCollection()) is None


def test_oldest_empty():

    analyzer = TickAnalyzer()

    assert analyzer.oldest(TickCollection()) is None


def test_find_empty():

    analyzer = TickAnalyzer()

    assert analyzer.find(
        TickCollection(),
        "EURUSD",
    ) is None


def test_price_distribution_empty():

    analyzer = TickAnalyzer()

    result = analyzer.price_distribution(
        TickCollection()
    )

    assert result == {}


def test_provider_analysis_empty():

    analyzer = TickAnalyzer()

    result = analyzer.provider_analysis(
        TickCollection()
    )

    assert result == {}


def test_symbol_analysis_empty():

    analyzer = TickAnalyzer()

    result = analyzer.symbol_analysis(
        TickCollection()
    )

    assert result == {}


def test_spread_analysis_empty():

    analyzer = TickAnalyzer()

    result = analyzer.spread_analysis(
        TickCollection()
    )

    assert result["average_spread"] == 0
    assert result["maximum_spread"] == 0
    assert result["minimum_spread"] == 0


def test_single_tick():

    analyzer = TickAnalyzer()

    collection = TickCollection()

    collection.append(

        Tick(
            symbol="EURUSD",
            timestamp=datetime.now(UTC),
            bid=1,
            ask=2,
            last=1.5,
            volume=10,
            provider=ProviderType.FYERS,
        )

    )

    result = analyzer.analyze(collection)

    assert result["count"] == 1
    assert result["total_volume"] == 10