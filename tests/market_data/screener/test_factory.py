"""
Tests for Screener factory.
"""

from ogs.market_data.screener import (
    Screener,
    ScreenerFactory,
    ScreenerStatus,
    ScreenerType,
)


def test_create():

    obj = ScreenerFactory.create(
        "SCR001",
        "SMC",
    )

    assert isinstance(obj, Screener)


def test_smart_money():

    obj = ScreenerFactory.smart_money(
        "SCR001",
        "SMC",
    )

    assert obj.screener_type == ScreenerType.SMART_MONEY
    assert obj.status == ScreenerStatus.ACTIVE


def test_ai():

    obj = ScreenerFactory.ai(
        "SCR002",
        "AI Screener",
    )

    assert obj.screener_type == ScreenerType.AI
    assert obj.status == ScreenerStatus.ACTIVE


def test_clone():

    obj = ScreenerFactory.create(
        "SCR001",
        "SMC",
    )

    clone = ScreenerFactory.clone(obj)

    assert clone == obj
    assert clone is not obj