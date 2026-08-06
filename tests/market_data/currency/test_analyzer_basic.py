"""
Tests for Currency analyzer.
"""

from ogs.market_data.currency import (
    Currency,
    CurrencyAnalyzer,
    CurrencyCollection,
)


def test_analyze():

    collection = CurrencyCollection()

    collection.add(
        Currency(
            currency_code="USD",
            numeric_code=840,
            name="US Dollar",
            is_fiat=True,
        )
    )

    analyzer = CurrencyAnalyzer()

    result = analyzer.analyze(collection)

    assert isinstance(result, dict)

    assert "summary" in result
    assert "currency_analysis" in result
    assert "distribution_analysis" in result