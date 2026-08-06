"""
Tests for Broker statistics.
"""

from ogs.market_data.broker import (
    Broker,
    BrokerCollection,
    BrokerStatistics,
    BrokerStatus,
)


def make_collection():

    collection = BrokerCollection()

    collection.add(
        Broker(
            broker_id="1",
            name="Broker One",
            status=BrokerStatus.ACTIVE,
        )
    )

    collection.add(
        Broker(
            broker_id="2",
            name="Broker Two",
            status=BrokerStatus.INACTIVE,
        )
    )

    return collection


def test_counts():

    stats = BrokerStatistics(
        make_collection()
    )

    assert stats.count == 2
    assert stats.active_count == 1
    assert stats.inactive_count == 1


def test_totals():

    stats = BrokerStatistics(
        make_collection()
    )

    assert stats.total_accounts == 0
    assert stats.total_equity == 0.0
    assert stats.total_cash == 0.0
    assert stats.total_buying_power == 0.0
    assert stats.total_margin_used == 0.0


def test_summary():

    stats = BrokerStatistics(
        make_collection()
    )

    summary = stats.summary()

    assert summary["count"] == 2
    assert summary["active_count"] == 1


def test_distribution():

    stats = BrokerStatistics(
        make_collection()
    )

    assert stats.status_distribution["ACTIVE"] == 1
    assert stats.status_distribution["INACTIVE"] == 1