"""
===========================================================

OGS Smart Money AI

Displacement Validator Tests

===========================================================
"""

import pytest

from ogs.smart_money.order_block.displacement import (
    DisplacementValidator,
)

from tests.factories import (
    make_displacement,
)


def test_validate():

    validator = DisplacementValidator()

    displacement = make_displacement()

    validator.validate(displacement)


def test_none():

    validator = DisplacementValidator()

    with pytest.raises(ValueError):

        validator.validate(None)