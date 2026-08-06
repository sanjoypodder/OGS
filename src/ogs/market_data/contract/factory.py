"""
OGS Smart Money AI

Contract Factory
"""

from __future__ import annotations

from copy import deepcopy

from .domain import Contract
from .enums import (
    ContractType,
    OptionType,
)


class ContractFactory:
    """
    Factory for Contract objects.
    """

    @staticmethod
    def create(
        contract_id: str,
        instrument_id: str,
        contract_symbol: str,
        exchange: str,
        underlying: str,
        **kwargs,
    ) -> Contract:

        return Contract(
            contract_id=contract_id,
            instrument_id=instrument_id,
            contract_symbol=contract_symbol,
            exchange=exchange,
            underlying=underlying,
            **kwargs,
        )

    @staticmethod
    def future(
        contract_id: str,
        instrument_id: str,
        contract_symbol: str,
        exchange: str,
        underlying: str,
        **kwargs,
    ) -> Contract:

        return Contract(
            contract_id=contract_id,
            instrument_id=instrument_id,
            contract_symbol=contract_symbol,
            exchange=exchange,
            underlying=underlying,
            contract_type=ContractType.FUTURE,
            **kwargs,
        )

    @staticmethod
    def call_option(
        contract_id: str,
        instrument_id: str,
        contract_symbol: str,
        exchange: str,
        underlying: str,
        **kwargs,
    ) -> Contract:

        return Contract(
            contract_id=contract_id,
            instrument_id=instrument_id,
            contract_symbol=contract_symbol,
            exchange=exchange,
            underlying=underlying,
            contract_type=ContractType.OPTION,
            option_type=OptionType.CALL,
            **kwargs,
        )

    @staticmethod
    def put_option(
        contract_id: str,
        instrument_id: str,
        contract_symbol: str,
        exchange: str,
        underlying: str,
        **kwargs,
    ) -> Contract:

        return Contract(
            contract_id=contract_id,
            instrument_id=instrument_id,
            contract_symbol=contract_symbol,
            exchange=exchange,
            underlying=underlying,
            contract_type=ContractType.OPTION,
            option_type=OptionType.PUT,
            **kwargs,
        )

    @staticmethod
    def clone(
        contract: Contract,
    ) -> Contract:

        return deepcopy(contract)