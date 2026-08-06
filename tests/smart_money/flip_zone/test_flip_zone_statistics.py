from decimal import Decimal

from ogs.smart_money.flip_zone.collection.flip_zone_collection import (
    FlipZoneCollection,
)
from ogs.smart_money.flip_zone.domain.flip_zone import FlipZone
from ogs.smart_money.flip_zone.statistics.flip_zone_statistics import (
    FlipZoneStatistics,
)


def test_statistics():

    collection = FlipZoneCollection()

    collection.add(
        FlipZone(
            upper_price=Decimal("110"),
            lower_price=Decimal("100"),
            flip_price=Decimal("105"),
            confidence=0.80,
            originating_bos_id="bos1",
            originating_swing_id="sw1",
        )
    )

    stats = FlipZoneStatistics(collection)

    assert stats.total == 1
    assert stats.average_confidence == 0.80