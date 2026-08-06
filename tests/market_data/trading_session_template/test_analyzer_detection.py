"""
Tests for TradingSessionTemplate analyzer detection.
"""

from ogs.market_data.trading_session_template import (
    TradingSessionTemplate,
    TradingSessionTemplateAnalyzer,
    TradingSessionTemplateCollection,
    TradingSessionTemplateStatus,
    TradingSessionTemplateType,
)


def test_distribution_detection():

    collection = TradingSessionTemplateCollection()

    collection.add(
        TradingSessionTemplate(
            trading_session_template_id="TST001",
            template_name="Regular",
            exchange="NSE",
            market="Equity",
            timezone="Asia/Kolkata",
            session_type=TradingSessionTemplateType.REGULAR,
            status=TradingSessionTemplateStatus.ACTIVE,
        )
    )

    collection.add(
        TradingSessionTemplate(
            trading_session_template_id="TST002",
            template_name="PreMarket",
            exchange="NYSE",
            market="Equity",
            timezone="America/New_York",
            session_type=TradingSessionTemplateType.PRE_MARKET,
            status=TradingSessionTemplateStatus.ACTIVE,
        )
    )

    analyzer = TradingSessionTemplateAnalyzer()

    result = analyzer.analyze(collection)

    distribution = result["distribution_analysis"]

    assert distribution["session_type"]["REGULAR"] == 1
    assert distribution["session_type"]["PRE_MARKET"] == 1