"""
Swing Enum Tests
"""

from ogs.smart_money.swing import SwingType


def test_high():
    assert SwingType.HIGH.value == "HIGH"


def test_low():
    assert SwingType.LOW.value == "LOW"


def test_enum_count():
    assert len(SwingType) == 2