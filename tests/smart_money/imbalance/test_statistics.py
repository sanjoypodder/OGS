from ogs.smart_money.imbalance import (
    ImbalanceSeries,
    ImbalanceStatistics,
)

from tests.factories import (
    make_bullish_imbalance,
    make_bearish_imbalance,
)


def test_empty():

    series = ImbalanceSeries()

    stats = ImbalanceStatistics(series)

    assert stats.total == 0
    assert stats.bullish == 0
    assert stats.bearish == 0


def test_total():

    series = ImbalanceSeries()

    series.append(make_bullish_imbalance())
    series.append(make_bearish_imbalance())

    stats = ImbalanceStatistics(series)

    assert stats.total == 2


def test_bullish():

    series = ImbalanceSeries()

    series.append(make_bullish_imbalance())
    series.append(make_bullish_imbalance())

    stats = ImbalanceStatistics(series)

    assert stats.bullish == 2


def test_bearish():

    series = ImbalanceSeries()

    series.append(make_bearish_imbalance())
    series.append(make_bearish_imbalance())

    stats = ImbalanceStatistics(series)

    assert stats.bearish == 2