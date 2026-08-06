"""
Tests for TradingSessionTemplate analyzer edge cases.
"""

from ogs.market_data.trading_session_template import (
    TradingSessionTemplateAnalyzer,
    TradingSessionTemplateCollection,
)


def test_empty_collection():

    analyzer = TradingSessionTemplateAnalyzer()

    result = analyzer.analyze(
        TradingSessionTemplateCollection()
    )

    assert result["summary"]["count"] == 0

    assert (
        result["trading_session_template_analysis"][
            "total_templates"
        ]
        == 0
    )


def test_empty_distribution():

    analyzer = TradingSessionTemplateAnalyzer()

    result = analyzer.analyze(
        TradingSessionTemplateCollection()
    )

    assert isinstance(
        result["distribution_analysis"]["session_type"],
        dict,
    )