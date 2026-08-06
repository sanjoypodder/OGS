"""
Tests for Index analyzer.
"""

from ogs.market_data.index import (
    Index,
    IndexAnalyzer,
    IndexCollection,
    IndexStatus,
    IndexType,
)


def test_analyze():

    collection = IndexCollection()

    collection.add(
        Index(
            index_code="NIFTY50",
            index_name="NIFTY 50",
            exchange="NSE",
            index_type=IndexType.BROAD_MARKET,
            status=IndexStatus.ACTIVE,
        )
    )

    analyzer = IndexAnalyzer()

    result = analyzer.analyze(collection)

    assert isinstance(result, dict)

    assert "summary" in result
    assert "index_analysis" in result
    assert "distribution_analysis" in result