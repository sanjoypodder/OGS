"""
Tests for TradingSessionTemplate analyzer performance.
"""

from ogs.market_data.trading_session_template import (
    TradingSessionTemplate,
    TradingSessionTemplateAnalyzer,
    TradingSessionTemplateCollection,
    TradingSessionTemplateStatus,
    TradingSessionTemplateType,
)


def test_large_collection():

    collection = TradingSessionTemplateCollection()

    for i in range(1000):

        collection.add(
            TradingSessionTemplate(
                trading_session_template_id=f"TST{i}",
                template_name=f"Template {i}",
                exchange="NSE",
                market="Equity",
                timezone="Asia/Kolkata",
                session_type=TradingSessionTemplateType.REGULAR,
                status=TradingSessionTemplateStatus.ACTIVE,
            )
        )

    analyzer = TradingSessionTemplateAnalyzer()

    result = analyzer.analyze(collection)

    assert result["summary"]["count"] == 1000

    assert (
        result["trading_session_template_analysis"][
            "total_templates"
        ]
        == 1000
    )

    assert (
        result["trading_session_template_analysis"][
            "active_templates"
        ]
        == 1000
    )

    assert (
        result["trading_session_template_analysis"][
            "exchange_distribution"
        ]["NSE"]
        == 1000
    )