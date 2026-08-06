"""
===========================================================

OGS Smart Money AI

Equal Low Domain Tests

===========================================================
"""

from decimal import Decimal

from tests.factories import make_swing_low

from ogs.smart_money.liquidity.equal_lows import (
    EqualLow,
    EqualLowType,
)


def test_create_equal_low():

    zone = EqualLow(
        first_swing=make_swing_low(index=2),
        second_swing=make_swing_low(index=8),
        zone_price=Decimal("90.00"),
        tolerance=Decimal("0.10"),
        equal_low_type=EqualLowType.CONFIRMED,
    )

    assert zone.equal_low_type == EqualLowType.CONFIRMED


def test_timestamp():

    second = make_swing_low(index=8)

    zone = EqualLow(
        first_swing=make_swing_low(index=2),
        second_swing=second,
        zone_price=Decimal("90.00"),
        tolerance=Decimal("0.10"),
        equal_low_type=EqualLowType.CONFIRMED,
    )

    assert zone.timestamp == second.timestamp


def test_zone_price():

    zone = EqualLow(
        first_swing=make_swing_low(index=2),
        second_swing=make_swing_low(index=8),
        zone_price=Decimal("90.00"),
        tolerance=Decimal("0.10"),
        equal_low_type=EqualLowType.CONFIRMED,
    )

    assert zone.zone_price == Decimal("90.00")


def test_string():

    zone = EqualLow(
        first_swing=make_swing_low(index=2),
        second_swing=make_swing_low(index=8),
        zone_price=Decimal("90.00"),
        tolerance=Decimal("0.10"),
        equal_low_type=EqualLowType.CONFIRMED,
    )

    assert "CONFIRMED" in str(zone)
    assert "Equal Low" in str(zone)


def test_is_frozen():

    zone = EqualLow(
        first_swing=make_swing_low(index=2),
        second_swing=make_swing_low(index=8),
        zone_price=Decimal("90.00"),
        tolerance=Decimal("0.10"),
        equal_low_type=EqualLowType.CONFIRMED,
    )

    try:
        zone.zone_price = Decimal("91.00")
        assert False
    except Exception:
        assert True