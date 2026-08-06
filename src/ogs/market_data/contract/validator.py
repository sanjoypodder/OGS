"""
===========================================================

OGS Smart Money AI

Contract Validator

===========================================================
"""

from __future__ import annotations

from datetime import datetime

from ogs.smart_money.base.validator import BaseValidator

from .domain import Contract
from .enums import (
    ContractStatus,
    ContractType,
    ExerciseStyle,
    OptionType,
    SettlementType,
)


class ContractValidator(
    BaseValidator[Contract],
):
    """
    Validator for Contract.
    """

    def validate(
        self,
        contract: Contract,
    ) -> None:

        if (
            not isinstance(contract.contract_id, str)
            or not contract.contract_id.strip()
        ):
            raise ValueError("Invalid contract_id.")

        if (
            not isinstance(contract.instrument_id, str)
            or not contract.instrument_id.strip()
        ):
            raise ValueError("Invalid instrument_id.")

        if (
            not isinstance(contract.contract_symbol, str)
            or not contract.contract_symbol.strip()
        ):
            raise ValueError("Invalid contract_symbol.")

        if (
            not isinstance(contract.exchange, str)
            or not contract.exchange.strip()
        ):
            raise ValueError("Invalid exchange.")

        if (
            not isinstance(contract.underlying, str)
            or not contract.underlying.strip()
        ):
            raise ValueError("Invalid underlying.")

        if not isinstance(
            contract.contract_type,
            ContractType,
        ):
            raise ValueError("Invalid contract type.")

        if not isinstance(
            contract.option_type,
            OptionType,
        ):
            raise ValueError("Invalid option type.")

        if not isinstance(
            contract.settlement_type,
            SettlementType,
        ):
            raise ValueError("Invalid settlement type.")

        if not isinstance(
            contract.exercise_style,
            ExerciseStyle,
        ):
            raise ValueError("Invalid exercise style.")

        if not isinstance(
            contract.status,
            ContractStatus,
        ):
            raise ValueError("Invalid contract status.")

        if (
            not isinstance(contract.currency, str)
            or not contract.currency.strip()
        ):
            raise ValueError("Invalid currency.")

        if contract.tick_size <= 0:
            raise ValueError("Invalid tick_size.")

        if contract.lot_size <= 0:
            raise ValueError("Invalid lot_size.")

        if contract.multiplier <= 0:
            raise ValueError("Invalid multiplier.")

        if contract.strike_price < 0:
            raise ValueError("Invalid strike_price.")

        if (
            contract.expiry is not None
            and not isinstance(
                contract.expiry,
                datetime,
            )
        ):
            raise ValueError("Invalid expiry.")

        return None