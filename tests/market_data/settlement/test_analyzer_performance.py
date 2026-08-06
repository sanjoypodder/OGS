"""
Tests for Settlement analyzer performance.
"""

from ogs.market_data.settlement import (
    Settlement,
    SettlementAnalyzer,
    SettlementCollection,
    SettlementCycle,
    SettlementStatus,
    SettlementType,
)


def test_large_collection():

    collection = SettlementCollection()

    for i in range(1000):

        collection.add(
            Settlement(
                settlement_id=f"SET{i}",
                exchange="NSE",
                market="Equity",
                instrument=f"SYM{i}",
                settlement_cycle=SettlementCycle.T1,
                settlement_type=SettlementType.CASH,
                status=SettlementStatus.ACTIVE,
            )
        )

    analyzer = SettlementAnalyzer()

    result = analyzer.analyze(collection)

    assert (
        result["summary"]["count"]
        == 1000
    )

    assert (
        result["settlement_analysis"][
            "total_settlements"
        ]
        == 1000
    )

    assert (
        result["settlement_analysis"][
            "active_settlements"
        ]
        == 1000
    )

    assert (
        result["settlement_analysis"][
            "exchange_distribution"
        ]["NSE"]
        == 1000
    )