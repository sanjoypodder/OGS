"""
Tests for the Quote package.
"""

from ogs.market_data.quote import (
    Quote,
    QuoteAnalyzer,
    QuoteCollection,
    QuoteFactory,
    QuoteStatistics,
    QuoteStatus,
    QuoteType,
    QuoteValidator,
)


def test_package_imports():
    assert Quote is not None
    assert QuoteAnalyzer is not None
    assert QuoteCollection is not None
    assert QuoteFactory is not None
    assert QuoteStatistics is not None
    assert QuoteValidator is not None
    assert QuoteType is not None
    assert QuoteStatus is not None


def test_package_version():
    import ogs.market_data.quote as quote

    assert hasattr(quote, "__version__")
    assert isinstance(quote.__version__, str)