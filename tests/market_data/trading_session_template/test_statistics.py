"""
Tests for TradingSessionTemplate statistics.
"""

from ogs.market_data.trading_session_template import (
    TradingSessionTemplate,
    TradingSessionTemplateCollection,
    TradingSessionTemplateStatistics,
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


def build_collection():

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
            "NSE",
            "Equity",
            TradingSessionTemplateType.PRE_MARKET,
            TradingSessionTemplateStatus.ACTIVE,
        )
    )

    collection.add(
        make(
            "TST003",
            "NYSE",
            "Equity",
            TradingSessionTemplateType.REGULAR,
            TradingSessionTemplateStatus.INACTIVE,
        )
    )

    return collection


def test_counts():

    stats = TradingSessionTemplateStatistics(
        build_collection()
    )

    assert stats.count == 3
    assert stats.active_count == 2


def test_exchange_distribution():

    stats = TradingSessionTemplateStatistics(
        build_collection()
    )

    distribution = stats.exchange_distribution()

    assert distribution["NSE"] == 2
    assert distribution["NYSE"] == 1


def test_market_distribution():

    stats = TradingSessionTemplateStatistics(
        build_collection()
    )

    distribution = stats.market_distribution()

    assert distribution["Equity"] == 3


def test_session_distribution():

    stats = TradingSessionTemplateStatistics(
        build_collection()
    )

    distribution = stats.session_type_distribution()

    assert distribution["REGULAR"] == 2
    assert distribution["PRE_MARKET"] == 1


def test_summary():

    stats = TradingSessionTemplateStatistics(
        build_collection()
    )

    summary = stats.summary()

    assert summary["count"] == 3
    assert summary["active"] == 2