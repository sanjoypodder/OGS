"""
Tests for Settlement collection.
"""

from ogs.market_data.settlement import (
    Settlement,
    SettlementCollection,
    SettlementCycle,
    SettlementStatus,
    SettlementType,
)


def make(
    settlement_id,
    exchange,
    market,
    instrument,
    cycle,
    settlement_type,
    status,
):

    return Settlement(
        settlement_id=settlement_id,
        exchange=exchange,
        market=market,
        instrument=instrument,
        settlement_cycle=cycle,
        settlement_type=settlement_type,
        status=status,
    )


def test_add():

    collection = SettlementCollection()

    collection.add(
        make(
            "SET001",
            "NSE",
            "Equity",
            "INFY",
            SettlementCycle.T1,
            SettlementType.CASH,
            SettlementStatus.ACTIVE,
        )
    )

    assert len(collection) == 1


def test_find():

    collection = SettlementCollection()

    obj = make(
        "SET001",
        "NSE",
        "Equity",
        "INFY",
        SettlementCycle.T1,
        SettlementType.CASH,
        SettlementStatus.ACTIVE,
    )

    collection.add(obj)

    assert collection.find("SET001") == obj
    assert collection.find("UNKNOWN") is None


def test_by_exchange():

    collection = SettlementCollection()

    collection.add(
        make(
            "SET001",
            "NSE",
            "Equity",
            "INFY",
            SettlementCycle.T1,
            SettlementType.CASH,
            SettlementStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "SET002",
            "NSE",
            "Derivatives",
            "NIFTY",
            SettlementCycle.T0,
            SettlementType.NET,
            SettlementStatus.ACTIVE,
        )
    )

    assert len(collection.by_exchange("NSE")) == 2


def test_by_market():

    collection = SettlementCollection()

    collection.add(
        make(
            "SET001",
            "NSE",
            "Equity",
            "INFY",
            SettlementCycle.T1,
            SettlementType.CASH,
            SettlementStatus.ACTIVE,
        )
    )

    assert len(collection.by_market("Equity")) == 1


def test_by_instrument():

    collection = SettlementCollection()

    collection.add(
        make(
            "SET001",
            "NSE",
            "Equity",
            "INFY",
            SettlementCycle.T1,
            SettlementType.CASH,
            SettlementStatus.ACTIVE,
        )
    )

    assert len(collection.by_instrument("INFY")) == 1


def test_by_cycle():

    collection = SettlementCollection()

    collection.add(
        make(
            "SET001",
            "NSE",
            "Equity",
            "INFY",
            SettlementCycle.T1,
            SettlementType.CASH,
            SettlementStatus.ACTIVE,
        )
    )

    assert len(collection.by_cycle(SettlementCycle.T1)) == 1


def test_by_type():

    collection = SettlementCollection()

    collection.add(
        make(
            "SET001",
            "NSE",
            "Equity",
            "INFY",
            SettlementCycle.T1,
            SettlementType.CASH,
            SettlementStatus.ACTIVE,
        )
    )

    assert len(collection.by_type(SettlementType.CASH)) == 1


def test_active():

    collection = SettlementCollection()

    collection.add(
        make(
            "SET001",
            "NSE",
            "Equity",
            "INFY",
            SettlementCycle.T1,
            SettlementType.CASH,
            SettlementStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "SET002",
            "NYSE",
            "Equity",
            "AAPL",
            SettlementCycle.T2,
            SettlementType.PHYSICAL,
            SettlementStatus.INACTIVE,
        )
    )

    assert len(collection.active()) == 1


def test_to_list():

    collection = SettlementCollection()

    collection.add(
        make(
            "SET001",
            "NSE",
            "Equity",
            "INFY",
            SettlementCycle.T1,
            SettlementType.CASH,
            SettlementStatus.ACTIVE,
        )
    )

    assert len(collection.to_list()) == 1