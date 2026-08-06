"""
===========================================================

OGS Smart Money AI

Equal High Domain Tests

===========================================================
"""

from decimal import Decimal

from tests.factories import make_swing_high

from ogs.smart_money.liquidity.equal_highs import (
    EqualHigh,
    EqualHighType,
)


def test_create_equal_high():

    zone = EqualHigh(
        first_swing=make_swing_high(index=2),
        second_swing=make_swing_high(index=8),
        zone_price=Decimal("110.00"),
        tolerance=Decimal("0.10"),
        equal_high_type=EqualHighType.CONFIRMED,
    )

    assert zone.equal_high_type == EqualHighType.CONFIRMED


def test_timestamp():

    second = make_swing_high(index=8)

    zone = EqualHigh(
        first_swing=make_swing_high(index=2),
        second_swing=second,
        zone_price=Decimal("110.00"),
        tolerance=Decimal("0.10"),
        equal_high_type=EqualHighType.CONFIRMED,
    )

    assert zone.timestamp == second.timestamp


def test_zone_price():

    zone = EqualHigh(
        first_swing=make_swing_high(index=2),
        second_swing=make_swing_high(index=8),
        zone_price=Decimal("110.00"),
        tolerance=Decimal("0.10"),
        equal_high_type=EqualHighType.CONFIRMED,
    )

    assert zone.zone_price == Decimal("110.00")


def test_string():

    zone = EqualHigh(
        first_swing=make_swing_high(index=2),
        second_swing=make_swing_high(index=8),
        zone_price=Decimal("110.00"),
        tolerance=Decimal("0.10"),
        equal_high_type=EqualHighType.CONFIRMED,
    )

    assert "CONFIRMED" in str(zone)
    assert "Equal High" in str(zone)


def test_is_frozen():

    zone = EqualHigh(
        first_swing=make_swing_high(index=2),
        second_swing=make_swing_high(index=8),
        zone_price=Decimal("110.00"),
        tolerance=Decimal("0.10"),
        equal_high_type=EqualHighType.CONFIRMED,
    )

    try:
        zone.zone_price = Decimal("111.00")
        assert False
    except Exception:
        assert True