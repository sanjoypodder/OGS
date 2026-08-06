"""
Tests for Contract domain.
"""

from ogs.market_data.contract import (
    Contract,
    ContractStatus,
    ContractType,
)


def test_default():

    obj = Contract()

    assert obj.contract_id == ""
    assert obj.instrument_id == ""
    assert obj.contract_symbol == ""
    assert obj.exchange == ""
    assert obj.underlying == ""

    assert obj.contract_type == ContractType.UNKNOWN
    assert obj.status == ContractStatus.ACTIVE

    assert obj.tick_size == 0.01
    assert obj.lot_size == 1

    assert obj.is_active
    assert not obj.is_tradable
    assert not obj.is_valid


def test_valid():

    obj = Contract(
        contract_id="1",
        instrument_id="INS1",
        contract_symbol="NIFTY24AUGFUT",
        exchange="NSE",
        underlying="NIFTY",
    )

    assert obj.is_valid


def test_tradable():

    obj = Contract(
        contract_id="1",
        instrument_id="INS1",
        contract_symbol="BTCUSDT-PERP",
        exchange="BINANCE",
        underlying="BTC",
        contract_type=ContractType.PERPETUAL,
    )

    assert obj.is_tradable


def test_to_dict():

    obj = Contract()

    data = obj.to_dict()

    assert isinstance(data, dict)
    assert "contract_id" in data


def test_str():

    obj = Contract()

    assert "Contract" in str(obj)