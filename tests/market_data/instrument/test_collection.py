"""
Tests for Instrument collection.
"""

from ogs.market_data.instrument import (
    Instrument,
    InstrumentCollection,
    InstrumentType,
)


def make(id_, t):

    return Instrument(
        instrument_id=id_,
        symbol=id_,
        exchange="TEST",
        asset=id_,
        name=id_,
        instrument_type=t,
    )


def test_add():

    c = InstrumentCollection()

    c.add(make("1", InstrumentType.EQUITY))

    assert len(c) == 1


def test_find():

    c = InstrumentCollection()

    x = make("BTC", InstrumentType.CRYPTO)

    c.add(x)

    assert c.find("BTC") == x
    assert c.find("XYZ") is None


def test_filters():

    c = InstrumentCollection()

    c.add(make("1", InstrumentType.EQUITY))
    c.add(make("2", InstrumentType.CRYPTO))
    c.add(make("3", InstrumentType.FOREX))
    c.add(make("4", InstrumentType.FUTURE))
    c.add(make("5", InstrumentType.OPTION))

    assert len(c.equities()) == 1
    assert len(c.crypto()) == 1
    assert len(c.forex()) == 1
    assert len(c.futures()) == 1
    assert len(c.options()) == 1


def test_to_list():

    c = InstrumentCollection()

    c.add(make("1", InstrumentType.EQUITY))

    assert len(c.to_list()) == 1