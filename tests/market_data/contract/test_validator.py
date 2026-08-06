"""
Tests for Contract validator.
"""

import pytest

from ogs.market_data.contract import (
    Contract,
    ContractType,
    ContractValidator,
)


def make():

    return Contract(
        contract_id="1",
        instrument_id="INS1",
        contract_symbol="BTCUSDT",
        exchange="BINANCE",
        underlying="BTC",
        contract_type=ContractType.SPOT,
    )


def test_success():

    validator = ContractValidator()

    assert validator.validate(make()) is None


@pytest.mark.parametrize(
    "field",
    [
        "contract_id",
        "instrument_id",
        "contract_symbol",
        "exchange",
        "underlying",
    ],
)
def test_required(field):

    obj = make()

    setattr(obj, field, "")

    validator = ContractValidator()

    with pytest.raises(ValueError):
        validator.validate(obj)


def test_tick():

    obj = make()

    obj.tick_size = 0

    validator = ContractValidator()

    with pytest.raises(ValueError):
        validator.validate(obj)


def test_lot():

    obj = make()

    obj.lot_size = 0

    validator = ContractValidator()

    with pytest.raises(ValueError):
        validator.validate(obj)


def test_multiplier():

    obj = make()

    obj.multiplier = 0

    validator = ContractValidator()

    with pytest.raises(ValueError):
        validator.validate(obj)


def test_negative_strike():

    obj = make()

    obj.strike_price = -1

    validator = ContractValidator()

    with pytest.raises(ValueError):
        validator.validate(obj)