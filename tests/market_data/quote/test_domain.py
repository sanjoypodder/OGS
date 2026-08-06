"""
Tests for Quote domain.
"""

from datetime import UTC
from datetime import datetime

from ogs.market_data.quote import (
    Quote,
    QuoteStatus,
    QuoteType,
)


def test_default_quote():

    q = Quote()

    assert q.name == ""
    assert q.bid == 0.0
    assert q.ask == 0.0
    assert q.last == 0.0
    assert q.volume == 0
    assert q.quote_type == QuoteType.UNKNOWN
    assert q.status == QuoteStatus.UNKNOWN


def test_spread():

    q = Quote(
        name="TEST",
        bid=100,
        ask=102,
    )

    assert q.spread == 2


def test_mid_price():

    q = Quote(
        name="TEST",
        bid=100,
        ask=102,
    )

    assert q.mid_price == 101


def test_mid_price_zero():

    q = Quote()

    assert q.mid_price == 0.0


def test_live_property():

    q = Quote(
        name="TEST",
        quote_type=QuoteType.LIVE,
    )

    assert q.is_live


def test_stale_property():

    q = Quote(
        name="TEST",
        status=QuoteStatus.STALE,
    )

    assert q.is_stale


def test_valid_quote():

    q = Quote(
        name="TEST",
        bid=100,
        ask=101,
        last=100.5,
    )

    assert q.is_valid


def test_invalid_quote():

    q = Quote()

    assert not q.is_valid


def test_to_dict():

    q = Quote(
        name="ABC",
        bid=100,
        ask=101,
    )

    data = q.to_dict()

    assert data["name"] == "ABC"
    assert data["quote_type"] == "UNKNOWN"
    assert data["status"] == "UNKNOWN"


def test_timestamp():

    q = Quote()

    assert isinstance(
        q.timestamp,
        datetime,
    )


def test_custom_timestamp():

    now = datetime.now(UTC)

    q = Quote(
        name="TEST",
        timestamp=now,
    )

    assert q.timestamp == now


def test_string():

    q = Quote(
        name="NIFTY",
        symbol="NSE:NIFTY50",
        last=25000,
    )

    s = str(q)

    assert "NIFTY" in s
    assert "25000" in s