from datetime import UTC, datetime
from zoneinfo import ZoneInfo

from ogs.market import Candle
from ogs.market import Price
from ogs.market import Symbol
from ogs.market import Timeframe
from ogs.market.analysis import TimezoneNormalizer
from ogs.market.collections import CandleSeries


def make(ts: datetime) -> Candle:
    return Candle(
        symbol=Symbol.XAUUSD,
        timeframe=Timeframe.M5,
        timestamp=ts,
        open=Price(Symbol.XAUUSD, 100),
        high=Price(Symbol.XAUUSD, 105),
        low=Price(Symbol.XAUUSD, 95),
        close=Price(Symbol.XAUUSD, 101),
    )


def test_already_utc():

    candle = make(datetime(2026, 1, 1, 12, 0, tzinfo=UTC))

    series = CandleSeries([candle])

    normalized, result = TimezoneNormalizer().analyze(series)

    assert result.normalized == 0
    assert result.skipped == 1
    assert normalized.first.timestamp.tzinfo == UTC


def test_convert_from_ist():

    ist = ZoneInfo("Asia/Kolkata")

    candle = make(datetime(2026, 1, 1, 17, 30, tzinfo=ist))

    series = CandleSeries([candle])

    normalized, result = TimezoneNormalizer().analyze(series)

    assert result.normalized == 1
    assert result.skipped == 0
    assert normalized.first.timestamp.tzinfo == UTC


def test_series_length():

    series = CandleSeries(
        [
            make(datetime(2026, 1, 1, 12, 0, tzinfo=UTC)),
            make(datetime(2026, 1, 1, 12, 5, tzinfo=UTC)),
        ]
    )

    normalized, _ = TimezoneNormalizer().analyze(series)

    assert len(normalized) == 2