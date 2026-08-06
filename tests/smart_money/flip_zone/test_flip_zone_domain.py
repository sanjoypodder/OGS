from decimal import Decimal

from ogs.smart_money.flip_zone.domain.flip_zone import FlipZone


def test_flip_zone_creation():

    zone = FlipZone(
        upper_price=Decimal("105"),
        lower_price=Decimal("100"),
        flip_price=Decimal("102"),
        originating_bos_id="bos1",
        originating_swing_id="sw1",
    )

    assert zone.upper_price == Decimal("105")
    assert zone.lower_price == Decimal("100")
    assert zone.flip_price == Decimal("102")


def test_midpoint():

    zone = FlipZone(
        upper_price=Decimal("110"),
        lower_price=Decimal("100"),
        flip_price=Decimal("105"),
        originating_bos_id="bos1",
        originating_swing_id="sw1",
    )

    assert zone.midpoint == Decimal("105")


def test_height():

    zone = FlipZone(
        upper_price=Decimal("110"),
        lower_price=Decimal("100"),
        flip_price=Decimal("105"),
        originating_bos_id="bos1",
        originating_swing_id="sw1",
    )

    assert zone.height == Decimal("10")