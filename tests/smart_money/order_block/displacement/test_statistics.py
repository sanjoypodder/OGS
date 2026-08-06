"""
===========================================================

OGS Smart Money AI

Displacement Statistics Tests

===========================================================
"""

from ogs.smart_money.order_block.displacement import (
    DisplacementDirection,
    DisplacementSeries,
    DisplacementStatistics,
)

from tests.factories import (
    make_displacement,
)


def test_total():

    series = DisplacementSeries(
        [
            make_displacement(),
            make_displacement(),
            make_displacement(),
        ]
    )

    statistics = DisplacementStatistics(series)

    assert statistics.total == 3


def test_empty():

    statistics = DisplacementStatistics(
        DisplacementSeries()
    )

    assert statistics.total == 0


def test_bullish():

    statistics = DisplacementStatistics(
        DisplacementSeries(
            [
                make_displacement(
                    DisplacementDirection.BULLISH
                ),
                make_displacement(
                    DisplacementDirection.BULLISH
                ),
            ]
        )
    )

    assert statistics.bullish == 2


def test_bearish():

    statistics = DisplacementStatistics(
        DisplacementSeries(
            [
                make_displacement(
                    DisplacementDirection.BEARISH
                ),
                make_displacement(
                    DisplacementDirection.BEARISH
                ),
            ]
        )
    )

    assert statistics.bearish == 2