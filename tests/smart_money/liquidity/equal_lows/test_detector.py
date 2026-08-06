"""
===========================================================

OGS Smart Money AI

Equal Low Detector Tests

===========================================================
"""

from decimal import Decimal

from ogs.smart_money.liquidity.equal_lows import (
    EqualLowDetector,
    EqualLowType,
)
from ogs.smart_money.swing import SwingSeries
from tests.factories import make_swing_low


def test_empty():

    detector = EqualLowDetector()

    result = detector.detect(
        SwingSeries([])
    )

    assert len(result) == 0


def test_single_swing():

    detector = EqualLowDetector()

    result = detector.detect(
        SwingSeries(
            [
                make_swing_low(index=2),
            ]
        )
    )

    assert len(result) == 0


def test_equal_low_detected():

    detector = EqualLowDetector()

    first = make_swing_low(index=2)
    second = make_swing_low(index=8)

    result = detector.detect(
        SwingSeries(
            [
                first,
                second,
            ]
        )
    )

    assert len(result) == 1

    zone = result.first

    assert zone.first_swing == first
    assert zone.second_swing == second
    assert zone.equal_low_type == EqualLowType.CONFIRMED
    assert zone.zone_price == Decimal("90.00")


def test_multiple_equal_lows():

    detector = EqualLowDetector()

    result = detector.detect(
        SwingSeries(
            [
                make_swing_low(index=2),
                make_swing_low(index=6),
                make_swing_low(index=10),
            ]
        )
    )

    assert len(result) == 2

from dataclasses import replace


def test_different_lows():

    detector = EqualLowDetector()

    first = make_swing_low(index=2)
    second = make_swing_low(index=8)

    second = replace(
        second,
        candle=replace(
            second.candle,
            low=second.candle.low.__class__(
                second.candle.symbol,
                80,
            ),
        ),
    )

    result = detector.detect(
        SwingSeries(
            [
                first,
                second,
            ]
        )
    )

    assert len(result) == 0

def test_boundary_tolerance():

    detector = EqualLowDetector()

    first = make_swing_low(index=2)
    second = make_swing_low(index=8)

    result = detector.detect(
        SwingSeries(
            [
                first,
                second,
            ]
        )
    )

    assert len(result) == 1