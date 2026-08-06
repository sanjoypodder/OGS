"""
===========================================================

OGS Smart Money AI

Order Block Candidate Validator

===========================================================
"""

from __future__ import annotations

from ogs.validation import (
    ValidationResult,
    ValidationStatus,
    Validator,
)

from .rules import OrderBlockRules


class OrderBlockCandidateValidator(
    Validator,
):
    """
    Validates an Order Block Candidate before
    confirmation.
    """

    def __init__(
        self,
        rules: OrderBlockRules | None = None,
    ):

        self._rules = (
            rules
            if rules is not None
            else OrderBlockRules()
        )

    def validate(
        self,
        candidate,
    ) -> ValidationResult:

        if candidate is None:

            return ValidationResult(
                status=ValidationStatus.INVALID,
                reason="Candidate is None",
            )

        if (
            self._rules.require_liquidity_sweep
            and candidate.liquidity_sweep is None
        ):

            return ValidationResult(
                status=ValidationStatus.INVALID,
                reason="Liquidity sweep required",
            )

        if (
            self._rules.require_mss
            and candidate.mss is None
        ):

            return ValidationResult(
                status=ValidationStatus.INVALID,
                reason="MSS required",
            )

        if candidate.origin_candle is None:

            return ValidationResult(
                status=ValidationStatus.INVALID,
                reason="Origin candle required",
            )

        return ValidationResult(
            status=ValidationStatus.VALID,
        )