"""
Tests for Market statistics.
"""

from ogs.market_data.market import (
    Market,
    MarketCollection,
    MarketStatistics,
    MarketStatus,
)


def make_collection():

    collection = MarketCollection()

    collection.add(
        Market(
            market_id="INDIA",
            name="Indian Market",
            status=MarketStatus.OPEN,
        )
    )

    collection.add(
        Market(
            market_id="USA",
            name="US Market",
            status=MarketStatus.CLOSED,
        )
    )

    return collection


def test_counts():

    stats = MarketStatistics(
        make_collection()
    )

    assert stats.count == 2
    assert stats.open_count == 1
    assert stats.closed_count == 1


def test_totals():

    stats = MarketStatistics(
        make_collection()
    )

    assert stats.exchange_count == 0
    assert stats.broker_count == 0
    assert stats.account_count == 0
    assert stats.total_equity == 0.0
    assert stats.total_cash == 0.0
    assert stats.total_buying_power == 0.0
    assert stats.total_margin_used == 0.0


def test_summary():

    stats = MarketStatistics(
        make_collection()
    )

    summary = stats.summary()

    assert summary["count"] == 2
    assert summary["open_count"] == 1
    assert summary["exchange_count"] == 0


def test_distribution():

    stats = MarketStatistics(
        make_collection()
    )

    assert stats.status_distribution["OPEN"] == 1
    assert stats.status_distribution["CLOSED"] == 1