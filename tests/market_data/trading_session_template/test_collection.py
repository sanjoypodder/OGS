"""
Tests for TradingSessionTemplate collection.
"""

from ogs.market_data.trading_session_template import (
    TradingSessionTemplate,
    TradingSessionTemplateCollection,
    TradingSessionTemplateStatus,
    TradingSessionTemplateType,
)


def make(
    template_id,
    exchange,
    market,
    session_type,
    status,
):

    return TradingSessionTemplate(
        trading_session_template_id=template_id,
        template_name=f"{exchange} Session",
        exchange=exchange,
        market=market,
        timezone="Asia/Kolkata",
        session_type=session_type,
        status=status,
    )


def test_add():

    collection = TradingSessionTemplateCollection()

    collection.add(
        make(
            "TST001",
            "NSE",
            "Equity",
            TradingSessionTemplateType.REGULAR,
            TradingSessionTemplateStatus.ACTIVE,
        )
    )

    assert len(collection) == 1


def test_find():

    collection = TradingSessionTemplateCollection()

    session = make(
        "TST001",
        "NSE",
        "Equity",
        TradingSessionTemplateType.REGULAR,
        TradingSessionTemplateStatus.ACTIVE,
    )

    collection.add(session)

    assert collection.find("TST001") == session
    assert collection.find("UNKNOWN") is None


def test_by_exchange():

    collection = TradingSessionTemplateCollection()

    collection.add(
        make(
            "TST001",
            "NSE",
            "Equity",
            TradingSessionTemplateType.REGULAR,
            TradingSessionTemplateStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "TST002",
            "NYSE",
            "Equity",
            TradingSessionTemplateType.REGULAR,
            TradingSessionTemplateStatus.ACTIVE,
        )
    )

    assert len(collection.by_exchange("NSE")) == 1


def test_by_market():

    collection = TradingSessionTemplateCollection()

    collection.add(
        make(
            "TST001",
            "NSE",
            "Equity",
            TradingSessionTemplateType.REGULAR,
            TradingSessionTemplateStatus.ACTIVE,
        )
    )

    assert len(collection.by_market("Equity")) == 1


def test_by_session_type():

    collection = TradingSessionTemplateCollection()

    collection.add(
        make(
            "TST001",
            "NSE",
            "Equity",
            TradingSessionTemplateType.REGULAR,
            TradingSessionTemplateStatus.ACTIVE,
        )
    )

    assert (
        len(
            collection.by_session_type(
                TradingSessionTemplateType.REGULAR
            )
        )
        == 1
    )


def test_active():

    collection = TradingSessionTemplateCollection()

    collection.add(
        make(
            "TST001",
            "NSE",
            "Equity",
            TradingSessionTemplateType.REGULAR,
            TradingSessionTemplateStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "TST002",
            "NYSE",
            "Equity",
            TradingSessionTemplateType.REGULAR,
            TradingSessionTemplateStatus.INACTIVE,
        )
    )

    assert len(collection.active()) == 1


def test_to_list():

    collection = TradingSessionTemplateCollection()

    collection.add(
        make(
            "TST001",
            "NSE",
            "Equity",
            TradingSessionTemplateType.REGULAR,
            TradingSessionTemplateStatus.ACTIVE,
        )
    )

    assert len(collection.to_list()) == 1