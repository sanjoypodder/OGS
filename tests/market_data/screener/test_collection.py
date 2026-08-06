"""
Tests for Screener collection.
"""

from ogs.market_data.screener import (
    Screener,
    ScreenerCollection,
    ScreenerStatus,
    ScreenerType,
)


def make(
    screener_id,
    name,
    screener_type,
    status,
):

    return Screener(
        screener_id=screener_id,
        screener_name=name,
        screener_type=screener_type,
        status=status,
    )


def test_add():

    collection = ScreenerCollection()

    collection.add(
        make(
            "SCR001",
            "SMC",
            ScreenerType.SMART_MONEY,
            ScreenerStatus.ACTIVE,
        )
    )

    assert len(collection) == 1


def test_find():

    collection = ScreenerCollection()

    obj = make(
        "SCR001",
        "SMC",
        ScreenerType.SMART_MONEY,
        ScreenerStatus.ACTIVE,
    )

    collection.add(obj)

    assert collection.find("SCR001") == obj
    assert collection.find("SCR999") is None


def test_by_type():

    collection = ScreenerCollection()

    collection.add(
        make(
            "SCR001",
            "SMC",
            ScreenerType.SMART_MONEY,
            ScreenerStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "SCR002",
            "AI",
            ScreenerType.AI,
            ScreenerStatus.ACTIVE,
        )
    )

    assert len(
        collection.by_type(
            ScreenerType.SMART_MONEY
        )
    ) == 1

    assert len(
        collection.by_type(
            ScreenerType.AI
        )
    ) == 1


def test_active():

    collection = ScreenerCollection()

    collection.add(
        make(
            "SCR001",
            "SMC",
            ScreenerType.SMART_MONEY,
            ScreenerStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "SCR002",
            "Archived",
            ScreenerType.SYSTEM,
            ScreenerStatus.INACTIVE,
        )
    )

    assert len(collection.active()) == 1


def test_to_list():

    collection = ScreenerCollection()

    collection.add(
        make(
            "SCR001",
            "SMC",
            ScreenerType.SMART_MONEY,
            ScreenerStatus.ACTIVE,
        )
    )

    assert len(collection.to_list()) == 1