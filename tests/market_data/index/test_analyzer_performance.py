"""
Tests for Index analyzer performance.
"""

from ogs.market_data.index import (
    Index,
    IndexAnalyzer,
    IndexCollection,
    IndexStatus,
    IndexType,
)


def test_large_collection():

    collection = IndexCollection()

    for i in range(1000):

        collection.add(
            Index(
                index_code=f"IDX{i}",
                index_name=f"Index {i}",
                exchange="NSE",
                index_type=IndexType.BROAD_MARKET,
                status=IndexStatus.ACTIVE,
            )
        )

    analyzer = IndexAnalyzer()

    result = analyzer.analyze(collection)

    assert result["summary"]["count"] == 1000

    assert (
        result["index_analysis"]["total_indices"]
        == 1000
    )

    assert (
        result["index_analysis"]["active_indices"]
        == 1000
    )