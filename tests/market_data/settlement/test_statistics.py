"""
Tests for Settlement statistics.
"""

from ogs.market_data.settlement import (
    Settlement,
    SettlementCollection,
    SettlementCycle,
    SettlementStatistics,
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


def build_collection():

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

    collection.add(
        make(
            "SET003",
            "NYSE",
            "Equity",
            "AAPL",
            SettlementCycle.T2,
            SettlementType.PHYSICAL,
            SettlementStatus.INACTIVE,
        )
    )

    return collection


def test_counts():

    stats = SettlementStatistics(
        build_collection()
    )

    assert stats.count == 3
    assert stats.active_count == 2


def test_exchange_distribution():

    stats = SettlementStatistics(
        build_collection()
    )

    distribution = (
        stats.exchange_distribution()
    )

    assert distribution["NSE"] == 2
    assert distribution["NYSE"] == 1


def test_market_distribution():

    stats = SettlementStatistics(
        build_collection()
    )

    distribution = (
        stats.market_distribution()
    )

    assert distribution["Equity"] == 2
    assert distribution["Derivatives"] == 1


def test_cycle_distribution():

    stats = SettlementStatistics(
        build_collection()
    )

    distribution = (
        stats.cycle_distribution()
    )

    assert distribution["T0"] == 1
    assert distribution["T1"] == 1
    assert distribution["T2"] == 1


def test_type_distribution():

    stats = SettlementStatistics(
        build_collection()
    )

    distribution = (
        stats.type_distribution()
    )

    assert distribution["CASH"] == 1
    assert distribution["NET"] == 1
    assert distribution["PHYSICAL"] == 1


def test_summary():

    stats = SettlementStatistics(
        build_collection()
    )

    summary = stats.summary()

    assert summary["count"] == 3
    assert summary["active"] == 2