"""
Tests for QuoteStatistics.
"""

from ogs.market_data.quote import (
    Quote,
    QuoteCollection,
    QuoteStatistics,
    QuoteStatus,
    QuoteType,
)


def quote(
    name,
    bid,
    ask,
    provider="NSE",
    quote_type=QuoteType.LIVE,
    status=QuoteStatus.ACTIVE,
):
    return Quote(
        name=name,
        bid=bid,
        ask=ask,
        provider=provider,
        quote_type=quote_type,
        status=status,
    )


def test_count():

    c = QuoteCollection()

    c.add(quote("A", 100, 101))
    c.add(quote("B", 200, 201))

    s = QuoteStatistics(c)

    assert s.count == 2


def test_active_inactive():

    c = QuoteCollection()

    c.add(quote("A", 100, 101))
    c.add(
        quote(
            "B",
            200,
            201,
            status=QuoteStatus.CLOSED,
        )
    )

    s = QuoteStatistics(c)

    assert s.active_count == 1
    assert s.inactive_count == 1


def test_average_spread():

    c = QuoteCollection()

    c.add(quote("A", 100, 102))
    c.add(quote("B", 200, 202))

    s = QuoteStatistics(c)

    assert s.average_spread == 2.0


def test_empty_average():

    c = QuoteCollection()

    s = QuoteStatistics(c)

    assert s.average_spread == 0.0


def test_type_distribution():

    c = QuoteCollection()

    c.add(quote("A", 1, 2))
    c.add(
        quote(
            "B",
            1,
            2,
            quote_type=QuoteType.HISTORICAL,
        )
    )

    s = QuoteStatistics(c)

    assert s.type_distribution["LIVE"] == 1
    assert s.type_distribution["HISTORICAL"] == 1


def test_status_distribution():

    c = QuoteCollection()

    c.add(quote("A", 1, 2))
    c.add(
        quote(
            "B",
            1,
            2,
            status=QuoteStatus.CLOSED,
        )
    )

    s = QuoteStatistics(c)

    assert s.status_distribution["ACTIVE"] == 1
    assert s.status_distribution["CLOSED"] == 1


def test_provider_distribution():

    c = QuoteCollection()

    c.add(quote("A", 1, 2, provider="NSE"))
    c.add(quote("B", 1, 2, provider="NSE"))
    c.add(quote("C", 1, 2, provider="BSE"))

    s = QuoteStatistics(c)

    assert s.provider_distribution["NSE"] == 2
    assert s.provider_distribution["BSE"] == 1


def test_summary():

    c = QuoteCollection()

    c.add(quote("A", 100, 101))

    summary = QuoteStatistics(c).summary()

    assert summary["count"] == 1
    assert "average_spread" in summary
    assert "provider_distribution" in summary