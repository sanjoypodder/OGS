"""
===========================================================

OGS Smart Money AI

Displacement Collection Tests

===========================================================
"""

from ogs.smart_money.order_block.displacement import (
    Displacement,
    DisplacementDirection,
    DisplacementSeries,
)

from tests.factories import make_bullish_candle


def make_displacement():

    return Displacement(
        candle=make_bullish_candle(),
        direction=DisplacementDirection.BULLISH,
    )


def test_create():

    series = DisplacementSeries()

    assert len(series) == 0


def test_append():

    series = DisplacementSeries()

    series.append(make_displacement())

    assert len(series) == 1


def test_first():

    displacement = make_displacement()

    series = DisplacementSeries([displacement])

    assert series.first == displacement


def test_last():

    displacement = make_displacement()

    series = DisplacementSeries([displacement])

    assert series.last == displacement


def test_latest():

    displacement1 = make_displacement()

    displacement2 = make_displacement()

    series = DisplacementSeries(
        [
            displacement1,
            displacement2,
        ]
    )

    latest = series.latest(1)

    assert len(latest) == 1
    assert latest.first == displacement2
def test_iteration():

    series = DisplacementSeries(
        [
            make_displacement(),
            make_displacement(),
        ]
    )

    assert len(list(series)) == 2


def test_indexing():

    displacement = make_displacement()

    series = DisplacementSeries([displacement])

    assert series[0] == displacement


def test_is_empty():

    assert DisplacementSeries().is_empty


def test_not_empty():

    assert not DisplacementSeries(
        [
            make_displacement(),
        ]
    ).is_empty