from decimal import Decimal

from ogs.smart_money.flip_zone.collection.flip_zone_collection import (
    FlipZoneCollection,
)
from ogs.smart_money.flip_zone.domain.flip_zone import FlipZone


def create_zone():

    return FlipZone(
        upper_price=Decimal("110"),
        lower_price=Decimal("100"),
        flip_price=Decimal("105"),
        originating_bos_id="bos1",
        originating_swing_id="sw1",
    )


def test_add():

    collection = FlipZoneCollection()

    collection.add(create_zone())

    assert len(collection) == 1


def test_clear():

    collection = FlipZoneCollection()

    collection.add(create_zone())

    collection.clear()

    assert len(collection) == 0