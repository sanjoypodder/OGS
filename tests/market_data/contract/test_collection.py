"""
Tests for Contract collection.
"""

from ogs.market_data.contract import (
    Contract,
    ContractCollection,
    ContractType,
)


def make(id_, t):

    return Contract(
        contract_id=id_,
        instrument_id=id_,
        contract_symbol=id_,
        exchange="TEST",
        underlying=id_,
        contract_type=t,
    )


def test_add():

    c = ContractCollection()

    c.add(make("1", ContractType.FUTURE))

    assert len(c) == 1


def test_find():

    c = ContractCollection()

    obj = make("BTC", ContractType.SPOT)

    c.add(obj)

    assert c.find("BTC") == obj
    assert c.find("XYZ") is None


def test_filters():

    c = ContractCollection()

    c.add(make("1", ContractType.FUTURE))
    c.add(make("2", ContractType.OPTION))
    c.add(make("3", ContractType.PERPETUAL))

    assert len(c.futures()) == 1
    assert len(c.options()) == 1
    assert len(c.perpetuals()) == 1


def test_to_list():

    c = ContractCollection()

    c.add(make("1", ContractType.SPOT))

    assert len(c.to_list()) == 1