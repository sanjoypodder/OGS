import pytest

from ogs.smart_money.rejection import (
    RejectionBlockValidator,
)

from tests.factories.rejection_factory import (
    make_bullish_rejection,
)


def test_valid():
    rejection = make_bullish_rejection()

    RejectionBlockValidator.validate(
        rejection
    )


def test_invalid_size():
    rejection = make_bullish_rejection()

    object.__setattr__(
        rejection,
        "size",
        -1,
    )

    with pytest.raises(ValueError):
        RejectionBlockValidator.validate(
            rejection
        )