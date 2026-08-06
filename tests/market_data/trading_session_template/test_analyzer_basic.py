"""
Tests for TradingSessionTemplate analyzer.
"""

from ogs.market_data.trading_session_template import (
    TradingSessionTemplate,
    TradingSessionTemplateAnalyzer,
    TradingSessionTemplateCollection,
    TradingSessionTemplateStatus,
    TradingSessionTemplateType,
)


def test_analyze():

    collection = TradingSessionTemplateCollection()

    collection.add(
        TradingSessionTemplate(
            trading_session_template_id="TST001",
            template_name="NSE Regular",
            exchange="NSE",
            market="Equity",
            timezone="Asia/Kolkata",
            session_type=TradingSessionTemplateType.REGULAR,
            status=TradingSessionTemplateStatus.ACTIVE,
        )
    )

    analyzer = TradingSessionTemplateAnalyzer()

    result = analyzer.analyze(collection)

    assert isinstance(result, dict)

    assert "summary" in result
    assert "trading_session_template_analysis" in result
    assert "distribution_analysis" in result