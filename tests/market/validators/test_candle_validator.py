from datetime import UTC, datetime
from decimal import Decimal

import pytest

from ogs.market import Candle, Price, Symbol, Timeframe
from ogs.market.validators import CandleValidator


def test_valid_candle():
    candle = Candle(
        symbol=Symbol.XAUUSD,
        timeframe=Timeframe.M5,
        timestamp=datetime(2026, 1, 1, 12, 0, tzinfo=UTC),
        open=Price(Symbol.XAUUSD, 100),
        high=Price(Symbol.XAUUSD, 105),
        low=Price(Symbol.XAUUSD, 95),
        close=Price(Symbol.XAUUSD, 101),
        volume=Decimal("1000"),
    )

    CandleValidator().validate(candle)


def test_timezone_required():
    candle = Candle(
        symbol=Symbol.XAUUSD,
        timeframe=Timeframe.M5,
        timestamp=datetime(2026, 1, 1, 12, 0),  # no tzinfo
        open=Price(Symbol.XAUUSD, 100),
        high=Price(Symbol.XAUUSD, 105),
        low=Price(Symbol.XAUUSD, 95),
        close=Price(Symbol.XAUUSD, 101),
    )

    with pytest.raises(ValueError):
        CandleValidator().validate(candle)