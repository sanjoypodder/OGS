"""
Tests for TradingHours collection.
"""

from ogs.market_data.trading_hours import (
    TradingHours,
    TradingHoursCollection,
    TradingHoursStatus,
    TradingHoursType,
)


def make(
    trading_hours_id,
    exchange,
    market,
    trading_hours_type,
    status,
):

    return TradingHours(
        trading_hours_id=trading_hours_id,
        exchange=exchange,
        market=market,
        session_name="Regular",
        trading_hours_type=trading_hours_type,
        status=status,
    )


def test_add():

    collection = TradingHoursCollection()

    collection.add(
        make(
            "TH001",
            "NSE",
            "Equity",
            TradingHoursType.REGULAR,
            TradingHoursStatus.ACTIVE,
        )
    )

    assert len(collection) == 1


def test_find():

    collection = TradingHoursCollection()

    obj = make(
        "TH001",
        "NSE",
        "Equity",
        TradingHoursType.REGULAR,
        TradingHoursStatus.ACTIVE,
    )

    collection.add(obj)

    assert collection.find("TH001") == obj
    assert collection.find("UNKNOWN") is None


def test_by_exchange():

    collection = TradingHoursCollection()

    collection.add(
        make(
            "TH001",
            "NSE",
            "Equity",
            TradingHoursType.REGULAR,
            TradingHoursStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "TH002",
            "NSE",
            "Derivatives",
            TradingHoursType.POST_MARKET,
            TradingHoursStatus.ACTIVE,
        )
    )

    assert len(collection.by_exchange("NSE")) == 2


def test_by_market():

    collection = TradingHoursCollection()

    collection.add(
        make(
            "TH001",
            "NSE",
            "Equity",
            TradingHoursType.REGULAR,
            TradingHoursStatus.ACTIVE,
        )
    )

    assert len(collection.by_market("Equity")) == 1


def test_by_type():

    collection = TradingHoursCollection()

    collection.add(
        make(
            "TH001",
            "NSE",
            "Equity",
            TradingHoursType.REGULAR,
            TradingHoursStatus.ACTIVE,
        )
    )

    assert len(
        collection.by_type(
            TradingHoursType.REGULAR
        )
    ) == 1


def test_active():

    collection = TradingHoursCollection()

    collection.add(
        make(
            "TH001",
            "NSE",
            "Equity",
            TradingHoursType.REGULAR,
            TradingHoursStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "TH002",
            "NYSE",
            "Equity",
            TradingHoursType.REGULAR,
            TradingHoursStatus.INACTIVE,
        )
    )

    assert len(collection.active()) == 1


def test_to_list():

    collection = TradingHoursCollection()

    collection.add(
        make(
            "TH001",
            "NSE",
            "Equity",
            TradingHoursType.REGULAR,
            TradingHoursStatus.ACTIVE,
        )
    )

    assert len(collection.to_list()) == 1