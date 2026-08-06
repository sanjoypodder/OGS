"""
Tests for Instrument validator.
"""

import pytest

from ogs.market_data.instrument import (
    Instrument,
    InstrumentType,
    InstrumentValidator,
)


def make():

    return Instrument(
        instrument_id="1",
        symbol="AAPL",
        exchange="NASDAQ",
        asset="AAPL",
        name="Apple",
        instrument_type=InstrumentType.EQUITY,
    )


def test_success():

    assert InstrumentValidator()(make())


@pytest.mark.parametrize(
    "field",
    [
        "instrument_id",
        "symbol",
        "exchange",
        "asset",
        "name",
    ],
)
def test_required(field):

    obj = make()

    setattr(obj, field, "")

    with pytest.raises(ValueError):
        InstrumentValidator()(obj)


def test_tick():

    obj = make()

    obj.tick_size = 0

    with pytest.raises(ValueError):
        InstrumentValidator()(obj)


def test_lot():

    obj = make()

    obj.lot_size = 0

    with pytest.raises(ValueError):
        InstrumentValidator()(obj)