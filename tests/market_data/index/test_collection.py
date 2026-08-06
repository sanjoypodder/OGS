"""
Tests for Index collection.
"""

from ogs.market_data.index import (
    Index,
    IndexCollection,
    IndexStatus,
    IndexType,
)


def make(
    code,
    name,
    index_type,
    status,
):

    return Index(
        index_code=code,
        index_name=name,
        exchange="NSE",
        index_type=index_type,
        status=status,
    )


def test_add():

    collection = IndexCollection()

    collection.add(
        make(
            "NIFTY50",
            "NIFTY 50",
            IndexType.BROAD_MARKET,
            IndexStatus.ACTIVE,
        )
    )

    assert len(collection) == 1


def test_find():

    collection = IndexCollection()

    obj = make(
        "NIFTY50",
        "NIFTY 50",
        IndexType.BROAD_MARKET,
        IndexStatus.ACTIVE,
    )

    collection.add(obj)

    assert collection.find("NIFTY50") == obj
    assert collection.find("BANKNIFTY") is None


def test_by_type():

    collection = IndexCollection()

    collection.add(
        make(
            "NIFTY50",
            "NIFTY 50",
            IndexType.BROAD_MARKET,
            IndexStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "NIFTYIT",
            "NIFTY IT",
            IndexType.SECTOR,
            IndexStatus.ACTIVE,
        )
    )

    assert len(
        collection.by_type(
            IndexType.BROAD_MARKET
        )
    ) == 1

    assert len(
        collection.by_type(
            IndexType.SECTOR
        )
    ) == 1


def test_active():

    collection = IndexCollection()

    collection.add(
        make(
            "NIFTY50",
            "NIFTY 50",
            IndexType.BROAD_MARKET,
            IndexStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "OLDINDEX",
            "Old Index",
            IndexType.SECTOR,
            IndexStatus.INACTIVE,
        )
    )

    assert len(collection.active()) == 1


def test_to_list():

    collection = IndexCollection()

    collection.add(
        make(
            "NIFTY50",
            "NIFTY 50",
            IndexType.BROAD_MARKET,
            IndexStatus.ACTIVE,
        )
    )

    assert len(collection.to_list()) == 1