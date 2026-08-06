"""
Tests for Exchange statistics.
"""

from ogs.market_data.exchange import (
    Exchange,
    ExchangeCollection,
    ExchangeStatistics,
    ExchangeStatus,
)


def make_collection():

    collection = ExchangeCollection()

    collection.add(
        Exchange(
            exchange_id="1",
            name="NSE",
            status=ExchangeStatus.OPEN,
        )
    )

    collection.add(
        Exchange(
            exchange_id="2",
            name="BSE",
            status=ExchangeStatus.CLOSED,
        )
    )

    return collection


def test_counts():

    stats = ExchangeStatistics(
        make_collection()
    )

    assert stats.count == 2
    assert stats.open_count == 1
    assert stats.closed_count == 1


def test_totals():

    stats = ExchangeStatistics(
        make_collection()
    )

    assert stats.total_brokers == 0
    assert stats.total_accounts == 0
    assert stats.total_equity == 0.0
    assert stats.total_cash == 0.0
    assert stats.total_buying_power == 0.0
    assert stats.total_margin_used == 0.0


def test_summary():

    stats = ExchangeStatistics(
        make_collection()
    )

    summary = stats.summary()

    assert summary["count"] == 2
    assert summary["open_count"] == 1


def test_distribution():

    stats = ExchangeStatistics(
        make_collection()
    )

    assert stats.status_distribution["OPEN"] == 1
    assert stats.status_distribution["CLOSED"] == 1