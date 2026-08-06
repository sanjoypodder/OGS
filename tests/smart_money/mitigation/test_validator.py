import pytest

from ogs.smart_money.mitigation import (
    MitigationBlockValidator,
)

from tests.factories.mitigation_factory import (
    make_bullish_mitigation,
)


def test_valid():
    mitigation = make_bullish_mitigation()

    MitigationBlockValidator.validate(
        mitigation
    )


def test_invalid_size():
    mitigation = make_bullish_mitigation()

    object.__setattr__(
        mitigation,
        "size",
        -1,
    )

    with pytest.raises(ValueError):
        MitigationBlockValidator.validate(
            mitigation
        )