"""
===========================================================

OGS Smart Money AI

Equal High Detector Tests

===========================================================
"""

from decimal import Decimal

from ogs.smart_money.liquidity.equal_highs import (
    EqualHighDetector,
    EqualHighType,
)
from ogs.smart_money.swing import SwingSeries
from tests.factories import make_swing_high


def test_empty():

    detector = EqualHighDetector()

    result = detector.detect(
        SwingSeries([])
    )

    assert len(result) == 0


def test_single_swing():

    detector = EqualHighDetector()

    result = detector.detect(
        SwingSeries(
            [
                make_swing_high(index=2),
            ]
        )
    )

    assert len(result) == 0


def test_equal_high_detected():

    detector = EqualHighDetector()

    first = make_swing_high(index=2)
    second = make_swing_high(index=8)

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
    assert zone.equal_high_type == EqualHighType.CONFIRMED
    assert zone.zone_price == Decimal("110.00")

def test_different_highs():

    detector = EqualHighDetector()

    first = make_swing_high(index=2)

    second = make_swing_high(index=8)

    # Make second swing clearly different
    from dataclasses import replace

    second = replace(
        second,
        candle=replace(
            second.candle,
            high=second.candle.high.__class__(
                second.candle.symbol,
                120,
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

def test_multiple_equal_highs():

    detector = EqualHighDetector()

    result = detector.detect(
        SwingSeries(
            [
                make_swing_high(index=2),
                make_swing_high(index=6),
                make_swing_high(index=10),
            ]
        )
    )

    assert len(result) == 2

def test_boundary_tolerance():

    detector = EqualHighDetector()

    first = make_swing_high(index=2)

    second = make_swing_high(index=8)

    result = detector.detect(
        SwingSeries(
            [
                first,
                second,
            ]
        )
    )

    assert len(result) == 1