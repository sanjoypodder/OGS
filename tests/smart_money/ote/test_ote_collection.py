"""
OGS FinOS

Unit Tests

OTE Collection
"""

from decimal import Decimal
from uuid import uuid4

from ogs.smart_money.ote.collection import (
    OTECollection,
)
from ogs.smart_money.ote.domain import (
    OTE,
)
from ogs.smart_money.ote.enums import (
    OTEDirection,
)


def create_ote(
    high="2100",
    low="2000",
) -> OTE:

    high = Decimal(high)
    low = Decimal(low)

    return OTE(
        range_high=high,
        range_low=low,
        level_62=high - Decimal("62"),
        level_705=high - Decimal("70.5"),
        level_79=high - Decimal("79"),
        zone_low=high - Decimal("79"),
        zone_high=high - Decimal("62"),
        direction=OTEDirection.BULLISH,
    )


def test_add():

    collection = OTECollection()

    ote = create_ote()

    collection.add(ote)

    assert len(collection) == 1


def test_extend():

    collection = OTECollection()

    first = create_ote()

    second = create_ote(
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

    collection = OTECollection()

    first = create_ote()

    second = create_ote(
        high="2200",
        low="2100",
    )

    collection.add(first)
    collection.add(second)

    assert collection.latest() == second


def test_get_by_id():

    collection = OTECollection()

    ote = create_ote()

    collection.add(ote)

    found = collection.get_by_id(
        ote.id
    )

    assert found == ote


def test_invalid_id():

    collection = OTECollection()

    assert collection.get_by_id(
        uuid4()
    ) is None


def test_clear():

    collection = OTECollection()

    collection.add(
        create_ote()
    )

    collection.clear()

    assert len(collection) == 0


def test_iteration():

    collection = OTECollection()

    collection.add(
        create_ote()
    )

    count = 0

    for _ in collection:
        count += 1

    assert count == 1


def test_indexing():

    collection = OTECollection()

    ote = create_ote()

    collection.add(ote)

    assert collection[0] == ote


def test_contains():

    collection = OTECollection()

    ote = create_ote()

    collection.add(ote)

    assert ote in collection


def test_bool():

    collection = OTECollection()

    assert bool(collection) is False

    collection.add(
        create_ote()
    )

    assert bool(collection) is True