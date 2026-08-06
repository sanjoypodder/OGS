"""
Tests for Instrument statistics.
"""

from ogs.market_data.instrument import (
    Instrument,
    InstrumentCollection,
    InstrumentStatistics,
    InstrumentType,
)


def collection():

    c = InstrumentCollection()

    c.add(
        Instrument(
            instrument_id="1",
            symbol="AAPL",
            exchange="NASDAQ",
            asset="AAPL",
            name="Apple",
            instrument_type=InstrumentType.EQUITY,
        )
    )

    c.add(
        Instrument(
            instrument_id="2",
            symbol="BTCUSDT",
            exchange="BINANCE",
            asset="BTC",
            name="Bitcoin",
            instrument_type=InstrumentType.CRYPTO,
        )
    )

    return c


def test_counts():

    s = InstrumentStatistics(collection())

    assert s.count == 2
    assert s.active_count == 2


def test_distribution():

    s = InstrumentStatistics(collection())

    assert s.equity_count == 1
    assert s.crypto_count == 1


def test_summary():

    s = InstrumentStatistics(collection())

    assert s.summary()["count"] == 2