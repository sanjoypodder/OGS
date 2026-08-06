"""
===========================================================

OGS Smart Money AI

CHOCH Enum Tests

===========================================================
"""

from ogs.smart_money.choch import CHOCHType


def test_bullish():

    assert CHOCHType.BULLISH.value == "BULLISH"


def test_bearish():

    assert CHOCHType.BEARISH.value == "BEARISH"


def test_enum_count():

    assert len(CHOCHType) == 2