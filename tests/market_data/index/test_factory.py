"""
Tests for Index factory.
"""

from ogs.market_data.index import (
    Index,
    IndexFactory,
    IndexStatus,
    IndexType,
)


def test_create():

    obj = IndexFactory.create(
        "NIFTY50",
        "NIFTY 50",
        "NSE",
    )

    assert isinstance(obj, Index)


def test_market_index():

    obj = IndexFactory.market_index(
        "NIFTY50",
        "NIFTY 50",
        "NSE",
    )

    assert obj.index_type == IndexType.BROAD_MARKET
    assert obj.status == IndexStatus.ACTIVE


def test_sector_index():

    obj = IndexFactory.sector_index(
        "NIFTYIT",
        "NIFTY IT",
        "NSE",
    )

    assert obj.index_type == IndexType.SECTOR
    assert obj.status == IndexStatus.ACTIVE


def test_clone():

    obj = IndexFactory.create(
        "NIFTY50",
        "NIFTY 50",
        "NSE",
    )

    clone = IndexFactory.clone(obj)

    assert clone == obj
    assert clone is not obj