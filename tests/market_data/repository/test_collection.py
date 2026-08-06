"""
Tests for RepositoryCollection.
"""

from ogs.market_data.repository import (
    RepositoryCollection,
    RepositoryFactory,
    RepositoryStatus,
)


def create_collection():

    return RepositoryCollection(
        [
            RepositoryFactory.create(
                name="Repo1",
                provider="FYERS",
                symbol="NIFTY",
                timeframe="1D",
                records=100,
            ),
            RepositoryFactory.create(
                name="Repo2",
                provider="FYERS",
                symbol="BANKNIFTY",
                timeframe="5m",
                status=RepositoryStatus.ACTIVE,
                records=200,
            ),
            RepositoryFactory.archive(
                "Archive"
            ),
        ]
    )


def test_length():

    collection = create_collection()

    assert len(collection) == 3


def test_find():

    collection = create_collection()

    repository = collection.find("Repo1")

    assert repository is not None
    assert repository.name == "Repo1"


def test_active():

    collection = create_collection()

    assert len(collection.active()) == 1


def test_archived():

    collection = create_collection()

    assert len(collection.archived()) == 1


def test_by_provider():

    collection = create_collection()

    assert len(collection.by_provider("FYERS")) == 2


def test_by_symbol():

    collection = create_collection()

    assert len(collection.by_symbol("NIFTY")) == 1


def test_largest():

    collection = create_collection()

    assert collection.largest().records == 200


def test_smallest():

    collection = create_collection()

    assert collection.smallest().records == 0


def test_total_records():

    collection = create_collection()

    assert collection.total_records() == 300


def test_average_records():

    collection = create_collection()

    assert collection.average_records() == 100