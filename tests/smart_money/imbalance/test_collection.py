"""
===========================================================

OGS Smart Money AI

Imbalance Collection Tests

===========================================================
"""

from ogs.smart_money.imbalance import (
    Imbalance,
    ImbalanceDirection,
    ImbalanceSeries,
)

from tests.factories import (
    make_bullish_candle,
)


def make_imbalance() -> Imbalance:

    return Imbalance(
        first=make_bullish_candle(),
        middle=make_bullish_candle(),
        last=make_bullish_candle(),
        direction=ImbalanceDirection.BULLISH,
    )


def test_empty():

    series = ImbalanceSeries()

    assert series.is_empty


def test_append():

    series = ImbalanceSeries()

    series.append(
        make_imbalance(),
    )

    assert len(series) == 1


def test_first():

    series = ImbalanceSeries()

    imbalance = make_imbalance()

    series.append(imbalance)

    assert series.first == imbalance


def test_last():

    series = ImbalanceSeries()

    imbalance = make_imbalance()

    series.append(imbalance)

    assert series.last == imbalance


def test_latest():

    series = ImbalanceSeries()

    series.append(make_imbalance())
    series.append(make_imbalance())
    series.append(make_imbalance())

    latest = series.latest(2)

    assert len(latest) == 2


def test_iteration():

    series = ImbalanceSeries()

    series.append(make_imbalance())
    series.append(make_imbalance())

    count = 0

    for _ in series:
        count += 1

    assert count == 2