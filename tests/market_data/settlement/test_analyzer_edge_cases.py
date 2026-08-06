"""
Tests for Settlement analyzer edge cases.
"""

from ogs.market_data.settlement import (
    SettlementAnalyzer,
    SettlementCollection,
)


def test_empty_collection():

    analyzer = SettlementAnalyzer()

    result = analyzer.analyze(
        SettlementCollection()
    )

    assert result["summary"]["count"] == 0
    assert (
        result["settlement_analysis"][
            "total_settlements"
        ]
        == 0
    )


def test_empty_distribution():

    analyzer = SettlementAnalyzer()

    result = analyzer.analyze(
        SettlementCollection()
    )

    distribution = result[
        "distribution_analysis"
    ]

    assert isinstance(
        distribution["settlement_cycle"],
        dict,
    )

    assert isinstance(
        distribution["settlement_type"],
        dict,
    )