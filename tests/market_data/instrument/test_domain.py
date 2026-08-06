"""
Tests for Instrument domain.
"""

from ogs.market_data.instrument import (
    Instrument,
    InstrumentStatus,
    InstrumentType,
)


def test_default():

    obj = Instrument()

    assert obj.instrument_id == ""
    assert obj.symbol == ""
    assert obj.exchange == ""
    assert obj.asset == ""
    assert obj.market == ""

    assert obj.instrument_type == InstrumentType.UNKNOWN
    assert obj.status == InstrumentStatus.ACTIVE

    assert obj.tick_size == 0.01
    assert obj.lot_size == 1

    assert obj.is_active
    assert not obj.is_tradable
    assert not obj.is_valid


def test_valid():

    obj = Instrument(
        instrument_id="1",
        symbol="AAPL",
        exchange="NASDAQ",
        asset="AAPL",
        name="Apple",
    )

    assert obj.is_valid


def test_tradable():

    obj = Instrument(
        instrument_id="1",
        symbol="BTCUSDT",
        exchange="BINANCE",
        asset="BTC",
        name="Bitcoin",
        instrument_type=InstrumentType.CRYPTO,
    )

    assert obj.is_tradable


def test_to_dict():

    obj = Instrument()

    data = obj.to_dict()

    assert isinstance(data, dict)
    assert "instrument_id" in data


def test_str():

    obj = Instrument()

    assert "Instrument" in str(obj)