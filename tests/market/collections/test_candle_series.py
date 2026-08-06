from datetime import UTC, datetime

from ogs.market import Candle
from ogs.market import Price
from ogs.market import Symbol
from ogs.market import Timeframe
from ogs.market.collections import CandleSeries


def make_candle(value: int) -> Candle:
    return Candle(
        symbol=Symbol.XAUUSD,
        timeframe=Timeframe.M5,
        timestamp=datetime(2026, 1, 1, 12, value, tzinfo=UTC),
        open=Price(Symbol.XAUUSD, value),
        high=Price(Symbol.XAUUSD, value + 2),
        low=Price(Symbol.XAUUSD, value - 2),
        close=Price(Symbol.XAUUSD, value + 1),
    )


def test_length():
    series = CandleSeries([make_candle(1), make_candle(2)])
    assert len(series) == 2


def test_first():
    series = CandleSeries([make_candle(1), make_candle(2)])
    assert series.first.open.value == Price(Symbol.XAUUSD, 1).value


def test_last():
    series = CandleSeries([make_candle(1), make_candle(2)])
    assert series.last.open.value == Price(Symbol.XAUUSD, 2).value


def test_previous():
    series = CandleSeries([make_candle(1), make_candle(2)])
    assert series.previous().open.value == Price(Symbol.XAUUSD, 1).value


def test_latest():
    series = CandleSeries(
        [make_candle(1), make_candle(2), make_candle(3)]
    )

    latest = series.latest(2)

    assert len(latest) == 2
    assert latest.first.open.value == Price(Symbol.XAUUSD, 2).value


def test_window():
    series = CandleSeries(
        [
            make_candle(1),
            make_candle(2),
            make_candle(3),
            make_candle(4),
        ]
    )

    window = series.window(1, 3)

    assert len(window) == 2
    assert window.first.open.value == Price(Symbol.XAUUSD, 2).value


def test_append():
    series = CandleSeries([])

    series.append(make_candle(10))

    assert len(series) == 1


def test_empty():
    assert CandleSeries([]).is_empty