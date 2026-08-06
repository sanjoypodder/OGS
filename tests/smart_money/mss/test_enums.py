"""
===========================================================

OGS Smart Money AI

MSS Enum Tests

===========================================================
"""

from ogs.smart_money.mss import MSSType


def test_bullish():

    assert MSSType.BULLISH.value == "BULLISH"


def test_bearish():

    assert MSSType.BEARISH.value == "BEARISH"


def test_enum_count():

    assert len(MSSType) == 2