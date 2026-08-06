"""
===========================================================

OGS Smart Money AI

Validator Tests

===========================================================
"""

from ogs.validation import (
    Validator,
    ValidationResult,
    ValidationStatus,
)


class DummyValidator(Validator):

    def validate(
        self,
        obj,
    ) -> ValidationResult:

        return ValidationResult(
            status=ValidationStatus.VALID,
        )


def test_validate():

    validator = DummyValidator()

    result = validator.validate(None)

    assert result.is_valid