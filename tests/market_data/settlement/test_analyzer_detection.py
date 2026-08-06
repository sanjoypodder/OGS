"""
Tests for Settlement analyzer detection.
"""

from ogs.market_data.settlement import (
    Settlement,
    SettlementAnalyzer,
    SettlementCollection,
    SettlementCycle,
    SettlementStatus,
    SettlementType,
)


def test_distribution_detection():

    collection = SettlementCollection()

    collection.add(
        Settlement(
            settlement_id="SET001",
            exchange="NSE",
            market="Equity",
            instrument="INFY",
            settlement_cycle=SettlementCycle.T1,
            settlement_type=SettlementType.CASH,
            status=SettlementStatus.ACTIVE,
        )
    )

    collection.add(
        Settlement(
            settlement_id="SET002",
            exchange="NYSE",
            market="Equity",
            instrument="AAPL",
            settlement_cycle=SettlementCycle.T2,
            settlement_type=SettlementType.PHYSICAL,
            status=SettlementStatus.ACTIVE,
        )
    )

    analyzer = SettlementAnalyzer()

    result = analyzer.analyze(collection)

    distribution = result[
        "distribution_analysis"
    ]

    assert (
        distribution["settlement_cycle"]["T1"]
        == 1
    )

    assert (
        distribution["settlement_cycle"]["T2"]
        == 1
    )

    assert (
        distribution["settlement_type"]["CASH"]
        == 1
    )

    assert (
        distribution["settlement_type"]["PHYSICAL"]
        == 1
    )