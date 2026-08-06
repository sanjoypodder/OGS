"""
===========================================================

OGS Smart Money AI

Currency Factory

===========================================================
"""

from __future__ import annotations

from .domain import Currency
from .enums import (
    CurrencyStatus,
    CurrencyType,
)
from .validator import CurrencyValidator


class CurrencyFactory:
    """
    Factory for creating validated Currency objects.
    """

    _validator = CurrencyValidator()

    @classmethod
    def create(
        cls,
        currency_code: str,
        numeric_code: int,
        name: str,
        currency_type: CurrencyType,
        status: CurrencyStatus = CurrencyStatus.ACTIVE,
        minor_unit: int = 2,
        exchange_rate: float = 1.0,
    ) -> Currency:
        """
        Create and validate a Currency instance.
        """

        currency = Currency(
            currency_code=currency_code.strip().upper(),
            numeric_code=numeric_code,
            name=name.strip(),
            currency_type=currency_type,
            status=status,
            minor_unit=minor_unit,
            exchange_rate=exchange_rate,
        )

        cls._validator.validate(currency)

        return currency

    @classmethod
    def fiat(
        cls,
        currency_code: str,
        numeric_code: int,
        name: str,
        minor_unit: int = 2,
        exchange_rate: float = 1.0,
    ) -> Currency:
        """
        Create an active fiat currency.
        """

        return cls.create(
            currency_code=currency_code,
            numeric_code=numeric_code,
            name=name,
            currency_type=CurrencyType.FIAT,
            status=CurrencyStatus.ACTIVE,
            minor_unit=minor_unit,
            exchange_rate=exchange_rate,
        )

    @classmethod
    def crypto(
        cls,
        currency_code: str,
        numeric_code: int,
        name: str,
        minor_unit: int = 8,
        exchange_rate: float = 1.0,
    ) -> Currency:
        """
        Create an active cryptocurrency.
        """

        return cls.create(
            currency_code=currency_code,
            numeric_code=numeric_code,
            name=name,
            currency_type=CurrencyType.CRYPTO,
            status=CurrencyStatus.ACTIVE,
            minor_unit=minor_unit,
            exchange_rate=exchange_rate,
        )

    @classmethod
    def digital(
        cls,
        currency_code: str,
        numeric_code: int,
        name: str,
        minor_unit: int = 2,
        exchange_rate: float = 1.0,
    ) -> Currency:
        """
        Create an active digital currency.
        """

        return cls.create(
            currency_code=currency_code,
            numeric_code=numeric_code,
            name=name,
            currency_type=CurrencyType.DIGITAL,
            status=CurrencyStatus.ACTIVE,
            minor_unit=minor_unit,
            exchange_rate=exchange_rate,
        )

    @classmethod
    def commodity(
        cls,
        currency_code: str,
        numeric_code: int,
        name: str,
        minor_unit: int = 2,
        exchange_rate: float = 1.0,
    ) -> Currency:
        """
        Create an active commodity-backed currency.
        """

        return cls.create(
            currency_code=currency_code,
            numeric_code=numeric_code,
            name=name,
            currency_type=CurrencyType.COMMODITY,
            status=CurrencyStatus.ACTIVE,
            minor_unit=minor_unit,
            exchange_rate=exchange_rate,
        )