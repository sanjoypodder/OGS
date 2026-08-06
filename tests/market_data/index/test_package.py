"""
Tests for Index package exports.
"""

from ogs.market_data.index import (
    __version__,
    Index,
    IndexAnalyzer,
    IndexCollection,
    IndexFactory,
    IndexStatistics,
    IndexStatus,
    IndexType,
    IndexValidator,
)


def test_version():

    assert __version__ == "0.1.0"


def test_exports():

    assert Index is not None
    assert IndexAnalyzer is not None
    assert IndexCollection is not None
    assert IndexFactory is not None
    assert IndexStatistics is not None
    assert IndexValidator is not None
    assert IndexType is not None
    assert IndexStatus is not None