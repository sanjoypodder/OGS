"""
Tests for OrderBookStatistics.
"""

from ogs.market_data.order_book import (
    OrderBook,
    OrderBookCollection,
    OrderBookStatistics,
    OrderBookStatus,
)


def book(
    name,
    bid,
    ask,
    provider="NSE",
    status=OrderBookStatus.ACTIVE,
):

    return OrderBook(
        name=name,
        best_bid=bid,
        best_ask=ask,
        provider=provider,
        status=status,
    )


def test_count():

    c = OrderBookCollection()

    c.add(book("A", 100, 101))

    s = OrderBookStatistics(c)

    assert s.count == 1


def test_active_inactive():

    c = OrderBookCollection()

    c.add(book("A", 100, 101))
    c.add(book("B", 100, 101, status=OrderBookStatus.CLOSED))

    s = OrderBookStatistics(c)

    assert s.active_count == 1
    assert s.inactive_count == 1


def test_average_spread():

    c = OrderBookCollection()

    c.add(book("A", 100, 102))
    c.add(book("B", 200, 202))

    s = OrderBookStatistics(c)

    assert s.average_spread == 2.0


def test_empty_average():

    c = OrderBookCollection()

    s = OrderBookStatistics(c)

    assert s.average_spread == 0.0


def test_type_distribution():

    c = OrderBookCollection()

    c.add(book("A", 1, 2))

    s = OrderBookStatistics(c)

    assert s.type_distribution["UNKNOWN"] == 1


def test_status_distribution():

    c = OrderBookCollection()

    c.add(book("A", 1, 2))

    s = OrderBookStatistics(c)

    assert s.status_distribution["ACTIVE"] == 1


def test_provider_distribution():

    c = OrderBookCollection()

    c.add(book("A", 1, 2, provider="NSE"))

    s = OrderBookStatistics(c)

    assert s.provider_distribution["NSE"] == 1


def test_summary():

    c = OrderBookCollection()

    c.add(book("A", 100, 101))

    s = OrderBookStatistics(c)

    summary = s.summary()

    assert summary["count"] == 1