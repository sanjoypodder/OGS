from datetime import UTC, datetime, timedelta

from ogs.market import Candle
from ogs.market import Price
from ogs.market import Symbol
from ogs.market import Timeframe
from ogs.market.analysis import GapDetector
from ogs.market.collections import CandleSeries


def make(ts: datetime) -> Candle:
    return Candle(
        symbol=Symbol.XAUUSD,
        timeframe=Timeframe.M5,
        timestamp=ts,
        open=Price(Symbol.XAUUSD, 100),
        high=Price(Symbol.XAUUSD, 101),
        low=Price(Symbol.XAUUSD, 99),
        close=Price(Symbol.XAUUSD, 100),
    )


def test_no_gap():

    start = datetime(2026, 1, 1, 12, 0, tzinfo=UTC)

    series = CandleSeries([
        make(start),
        make(start + timedelta(minutes=5)),
        make(start + timedelta(minutes=10)),
    ])

    assert GapDetector().analyze(series) == []


def test_gap():

    start = datetime(2026, 1, 1, 12, 0, tzinfo=UTC)

    series = CandleSeries([
        make(start),
        make(start + timedelta(minutes=5)),
        make(start + timedelta(minutes=15)),
    ])

    assert GapDetector().analyze(series) == [2]


def test_single():

    start = datetime(2026, 1, 1, 12, 0, tzinfo=UTC)

    series = CandleSeries([
        make(start),
    ])

    assert GapDetector().analyze(series) == []