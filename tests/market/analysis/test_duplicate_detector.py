from datetime import UTC, datetime

from ogs.market import Candle
from ogs.market import Price
from ogs.market import Symbol
from ogs.market import Timeframe
from ogs.market.analysis import DuplicateDetector
from ogs.market.collections import CandleSeries


def candle(ts: datetime) -> Candle:

    return Candle(
        symbol=Symbol.XAUUSD,
        timeframe=Timeframe.M5,
        timestamp=ts,
        open=Price(Symbol.XAUUSD, 100),
        high=Price(Symbol.XAUUSD, 105),
        low=Price(Symbol.XAUUSD, 95),
        close=Price(Symbol.XAUUSD, 101),
    )


def test_no_duplicates():

    start = datetime(2026, 1, 1, 12, 0, tzinfo=UTC)

    series = CandleSeries(
        [
            candle(start),
            candle(datetime(2026, 1, 1, 12, 5, tzinfo=UTC)),
            candle(datetime(2026, 1, 1, 12, 10, tzinfo=UTC)),
        ]
    )

    detector = DuplicateDetector()

    assert detector.analyze(series) == []


def test_one_duplicate():

    start = datetime(2026, 1, 1, 12, 0, tzinfo=UTC)

    duplicate = datetime(2026, 1, 1, 12, 5, tzinfo=UTC)

    series = CandleSeries(
        [
            candle(start),
            candle(duplicate),
            candle(duplicate),
        ]
    )

    detector = DuplicateDetector()

    result = detector.analyze(series)

    assert len(result) == 1
    assert result[0].index == 2


def test_multiple_duplicates():

    start = datetime(2026, 1, 1, 12, 0, tzinfo=UTC)

    duplicate = datetime(2026, 1, 1, 12, 5, tzinfo=UTC)

    series = CandleSeries(
        [
            candle(start),
            candle(duplicate),
            candle(duplicate),
            candle(duplicate),
        ]
    )

    detector = DuplicateDetector()

    result = detector.analyze(series)

    assert len(result) == 2