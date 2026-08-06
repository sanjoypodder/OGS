"""
===========================================================

OGS Smart Money AI

BOS Validator Tests

===========================================================
"""

import pytest

from ogs.smart_money.bos import BOSValidator


def test_valid(sample_bos):

    BOSValidator().validate(sample_bos)


def test_invalid():

    validator = BOSValidator()

    with pytest.raises(ValueError):
        validator.validate(None)