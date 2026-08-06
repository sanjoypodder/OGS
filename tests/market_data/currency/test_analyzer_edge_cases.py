"""
Currency analyzer edge case tests.
"""

from ogs.market_data.currency import (
    CurrencyAnalyzer,
    CurrencyCollection,
)


def test_empty_collection():

    analyzer = CurrencyAnalyzer()

    result = analyzer.analyze(
        CurrencyCollection()
    )

    assert result["summary"]["count"] == 0


def test_empty_distribution():

    analyzer = CurrencyAnalyzer()

    result = analyzer.analyze(
        CurrencyCollection()
    )

    distribution = result[
        "distribution_analysis"
    ]["currency_type"]

    assert isinstance(distribution, dict)