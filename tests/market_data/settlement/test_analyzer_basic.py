"""
Tests for Settlement analyzer.
"""

from ogs.market_data.settlement import (
    Settlement,
    SettlementAnalyzer,
    SettlementCollection,
    SettlementCycle,
    SettlementStatus,
    SettlementType,
)


def test_analyze():

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

    analyzer = SettlementAnalyzer()

    result = analyzer.analyze(collection)

    assert isinstance(result, dict)

    assert "summary" in result
    assert "settlement_analysis" in result
    assert "distribution_analysis" in result