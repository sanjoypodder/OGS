"""
Tests for Account analyzer edge cases.
"""

from ogs.market_data.account import (
    AccountAnalyzer,
    AccountCollection,
)


def test_empty_collection():

    analyzer = AccountAnalyzer(
        AccountCollection()
    )

    result = analyzer.analyze()

    assert result["summary"]["count"] == 0
    assert result["account_analysis"]["total_equity"] == 0.0


def test_empty_distribution():

    analyzer = AccountAnalyzer(
        AccountCollection()
    )

    distribution = analyzer.distribution_analysis()

    assert distribution["status"] == {}
    assert distribution["types"] == {}