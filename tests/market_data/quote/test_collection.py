"""
Tests for QuoteCollection.
"""

from ogs.market_data.quote import (
    Quote,
    QuoteCollection,
    QuoteStatus,
    QuoteType,
)


def make_quote(
    name,
    provider="NSE",
    symbol="NIFTY",
    quote_type=QuoteType.LIVE,
    status=QuoteStatus.ACTIVE,
):

    return Quote(
        name=name,
        provider=provider,
        symbol=symbol,
        quote_type=quote_type,
        status=status,
    )


def test_add():

    c = QuoteCollection()

    q = make_quote("A")

    c.add(q)

    assert len(c.items) == 1


def test_active():

    c = QuoteCollection()

    c.add(make_quote("A"))
    c.add(make_quote("B", status=QuoteStatus.STALE))

    assert len(c.active()) == 1


def test_inactive():

    c = QuoteCollection()

    c.add(make_quote("A"))
    c.add(make_quote("B", status=QuoteStatus.CLOSED))

    assert len(c.inactive()) == 1


def test_by_type():

    c = QuoteCollection()

    c.add(make_quote("A"))

    c.add(
        make_quote(
            "B",
            quote_type=QuoteType.HISTORICAL,
        )
    )

    assert len(c.by_type(QuoteType.LIVE)) == 1
    assert len(c.by_type(QuoteType.HISTORICAL)) == 1


def test_by_provider():

    c = QuoteCollection()

    c.add(make_quote("A", provider="NSE"))

    c.add(make_quote("B", provider="BSE"))

    assert len(c.by_provider("NSE")) == 1


def test_by_symbol():

    c = QuoteCollection()

    c.add(make_quote("A", symbol="AAPL"))

    c.add(make_quote("B", symbol="MSFT"))

    assert len(c.by_symbol("AAPL")) == 1


def test_find():

    c = QuoteCollection()

    q = make_quote("ABC")

    c.add(q)

    assert c.find("ABC") is q
    assert c.find("XYZ") is None


def test_total_active():

    c = QuoteCollection()

    c.add(make_quote("A"))
    c.add(make_quote("B"))

    assert c.total_active() == 2


def test_to_list():

    c = QuoteCollection()

    c.add(make_quote("A"))

    data = c.to_list()

    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["name"] == "A"