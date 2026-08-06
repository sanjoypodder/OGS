"""
OGS Smart Money AI
------------------

SMT Divergence Validator

Validates SMT Divergence domain objects.

Author : Om Ganapati Solution
Version: 1.0.0
"""

from ogs.smart_money.base.validator import BaseValidator

from .domain import SMTDivergence


class SMTDivergenceValidator(
    BaseValidator[SMTDivergence],
):
    """
    Validator for SMT Divergence objects.
    """

    def validate(
        self,
        divergence: SMTDivergence,
    ) -> bool:
        """
        Validate an SMT Divergence.

        Returns
        -------
        bool
            True if valid, otherwise False.
        """

        if divergence is None:
            return False

        if not divergence.first_symbol:
            return False

        if not divergence.second_symbol:
            return False

        if divergence.first_symbol == divergence.second_symbol:
            return False

        if divergence.first_price <= 0:
            return False

        if divergence.second_price <= 0:
            return False

        if divergence.direction is None:
            return False

        if divergence.comparison is None:
            return False

        if divergence.timestamp is None:
            return False

        if divergence.confidence is None:
            return False

        return True