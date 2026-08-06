"""
Tests for CacheCollection.
"""

from ogs.market_data.cache import (
    CacheCollection,
    CacheFactory,
    CacheStatus,
    CacheType,
)


def create_collection():

    return CacheCollection(
        [
            CacheFactory.create(
                name="Cache1",
                cache_type=CacheType.MEMORY,
                status=CacheStatus.ACTIVE,
                capacity=100,
                used=50,
            ),
            CacheFactory.create(
                name="Cache2",
                cache_type=CacheType.REDIS,
                status=CacheStatus.ACTIVE,
                capacity=200,
                used=100,
            ),
            CacheFactory.create(
                name="Expired",
                cache_type=CacheType.DISK,
                status=CacheStatus.EXPIRED,
                capacity=50,
                used=0,
            ),
        ]
    )


def test_length():

    collection = create_collection()

    assert len(collection) == 3


def test_find():

    collection = create_collection()

    cache = collection.find("Cache1")

    assert cache is not None
    assert cache.name == "Cache1"


def test_active():

    collection = create_collection()

    assert len(collection.active()) == 2


def test_expired():

    collection = create_collection()

    assert len(collection.expired()) == 1


def test_by_type():

    collection = create_collection()

    result = collection.by_type(
        CacheType.REDIS
    )

    assert len(result) == 1


def test_largest():

    collection = create_collection()

    assert collection.largest().capacity == 200


def test_smallest():

    collection = create_collection()

    assert collection.smallest().capacity == 50


def test_total_capacity():

    collection = create_collection()

    assert collection.total_capacity() == 350


def test_total_used():

    collection = create_collection()

    assert collection.total_used() == 150


def test_average_utilization():

    collection = create_collection()

    assert round(
    collection.average_utilization(),
    2,
    ) == 33.33