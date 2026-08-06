"""
Tests for Instrument factory.
"""

from ogs.market_data.instrument import (
    Instrument,
    InstrumentFactory,
    InstrumentType,
)


def test_create():

    obj = InstrumentFactory.create(
        "1",
        "AAPL",
        "NASDAQ",
        "AAPL",
        "Apple",
    )

    assert isinstance(obj, Instrument)


def test_equity():

    obj = InstrumentFactory.equity(
        "1",
        "AAPL",
        "NASDAQ",
        "AAPL",
        "Apple",
    )

    assert obj.instrument_type == InstrumentType.EQUITY


def test_crypto():

    obj = InstrumentFactory.crypto(
        "1",
        "BTCUSDT",
        "BINANCE",
        "BTC",
        "Bitcoin",
    )

    assert obj.instrument_type == InstrumentType.CRYPTO


def test_forex():

    obj = InstrumentFactory.forex(
        "1",
        "EURUSD",
        "FOREX",
        "EURUSD",
        "Euro Dollar",
    )

    assert obj.instrument_type == InstrumentType.FOREX


def test_clone():

    obj = InstrumentFactory.create(
        "1",
        "AAPL",
        "NASDAQ",
        "AAPL",
        "Apple",
    )

    clone = InstrumentFactory.clone(obj)

    assert clone == obj
    assert clone is not obj