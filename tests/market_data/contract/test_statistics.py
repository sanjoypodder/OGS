"""
Tests for Contract statistics.
"""

from ogs.market_data.contract import (
    Contract,
    ContractCollection,
    ContractStatistics,
    ContractType,
)


def collection():

    c = ContractCollection()

    c.add(
        Contract(
            contract_id="1",
            instrument_id="1",
            contract_symbol="FUT1",
            exchange="NSE",
            underlying="NIFTY",
            contract_type=ContractType.FUTURE,
        )
    )

    c.add(
        Contract(
            contract_id="2",
            instrument_id="2",
            contract_symbol="PERP",
            exchange="BINANCE",
            underlying="BTC",
            contract_type=ContractType.PERPETUAL,
        )
    )

    return c


def test_counts():

    s = ContractStatistics(collection())

    assert s.count == 2
    assert s.active_count == 2


def test_distribution():

    s = ContractStatistics(collection())

    assert s.future_count == 1
    assert s.perpetual_count == 1


def test_summary():

    s = ContractStatistics(collection())

    assert s.summary()["count"] == 2