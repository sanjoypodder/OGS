"""
Tests for Universe collection.
"""

from ogs.market_data.universe import (
    Universe,
    UniverseCollection,
    UniverseStatus,
    UniverseType,
)


def make(
    universe_id,
    name,
    universe_type,
    status,
):

    return Universe(
        universe_id=universe_id,
        universe_name=name,
        universe_type=universe_type,
        status=status,
    )


def test_add():

    collection = UniverseCollection()

    collection.add(
        make(
            "UNI001",
            "NIFTY50",
            UniverseType.INDEX,
            UniverseStatus.ACTIVE,
        )
    )

    assert len(collection) == 1


def test_find():

    collection = UniverseCollection()

    obj = make(
        "UNI001",
        "NIFTY50",
        UniverseType.INDEX,
        UniverseStatus.ACTIVE,
    )

    collection.add(obj)

    assert collection.find("UNI001") == obj
    assert collection.find("UNKNOWN") is None


def test_by_type():

    collection = UniverseCollection()

    collection.add(
        make(
            "UNI001",
            "NIFTY50",
            UniverseType.INDEX,
            UniverseStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "UNI002",
            "Favorites",
            UniverseType.WATCHLIST,
            UniverseStatus.ACTIVE,
        )
    )

    assert len(
        collection.by_type(
            UniverseType.INDEX
        )
    ) == 1

    assert len(
        collection.by_type(
            UniverseType.WATCHLIST
        )
    ) == 1


def test_active():

    collection = UniverseCollection()

    collection.add(
        make(
            "UNI001",
            "NIFTY50",
            UniverseType.INDEX,
            UniverseStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "UNI002",
            "Archive",
            UniverseType.CUSTOM,
            UniverseStatus.INACTIVE,
        )
    )

    assert len(collection.active()) == 1


def test_to_list():

    collection = UniverseCollection()

    collection.add(
        make(
            "UNI001",
            "NIFTY50",
            UniverseType.INDEX,
            UniverseStatus.ACTIVE,
        )
    )

    assert len(collection.to_list()) == 1