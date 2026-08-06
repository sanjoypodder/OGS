"""
OGS FinOS

Unit Tests

Dealing Range Collection
"""

from decimal import Decimal

from ogs.smart_money.dealing_range.collection import (
    DealingRangeCollection,
)
from ogs.smart_money.dealing_range.domain import (
    DealingRange,
)
from ogs.smart_money.dealing_range.enums import (
    DealingRangeDirection,
)


def create_range(
    high: str = "2100",
    low: str = "2000",
) -> DealingRange:
    return DealingRange(
        range_high=Decimal(high),
        range_low=Decimal(low),
        equilibrium=(
            Decimal(high) + Decimal(low)
        ) / Decimal("2"),
        direction=DealingRangeDirection.BULLISH,
        start_index=10,
        end_index=20,
    )


def test_add():

    collection = DealingRangeCollection()

    dealing_range = create_range()

    collection.add(dealing_range)

    assert len(collection) == 1


def test_extend():

    collection = DealingRangeCollection()

    first = create_range()

    second = create_range(
        high="2200",
        low="2100",
    )

    collection.extend(
        [
            first,
            second,
        ]
    )

    assert len(collection) == 2


def test_latest():

    collection = DealingRangeCollection()

    first = create_range()

    second = create_range(
        high="2200",
        low="2100",
    )

    collection.add(first)
    collection.add(second)

    assert collection.latest() == second


def test_get_by_id():

    collection = DealingRangeCollection()

    dealing_range = create_range()

    collection.add(dealing_range)

    found = collection.get_by_id(
        dealing_range.id
    )

    assert found == dealing_range


def test_get_by_invalid_id():

    from uuid import uuid4

    collection = DealingRangeCollection()

    assert (
        collection.get_by_id(
            uuid4()
        )
        is None
    )


def test_clear():

    collection = DealingRangeCollection()

    collection.add(create_range())

    collection.clear()

    assert len(collection) == 0


def test_iteration():

    collection = DealingRangeCollection()

    collection.add(create_range())

    count = 0

    for _ in collection:
        count += 1

    assert count == 1


def test_indexing():

    collection = DealingRangeCollection()

    dealing_range = create_range()

    collection.add(dealing_range)

    assert collection[0] == dealing_range


def test_contains():

    collection = DealingRangeCollection()

    dealing_range = create_range()

    collection.add(dealing_range)

    assert dealing_range in collection


def test_bool():

    collection = DealingRangeCollection()

    assert bool(collection) is False

    collection.add(create_range())

    assert bool(collection) is True