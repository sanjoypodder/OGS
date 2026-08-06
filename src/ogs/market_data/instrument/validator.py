"""
OGS Smart Money AI

Instrument Validator
"""

from __future__ import annotations

from datetime import datetime

from .domain import Instrument
from .enums import (
    InstrumentStatus,
    InstrumentType,
)


class InstrumentValidator:
    """
    Validator for Instrument.
    """

    def __call__(
        self,
        instrument: Instrument,
    ) -> bool:

        if (
            not isinstance(instrument.instrument_id, str)
            or not instrument.instrument_id.strip()
        ):
            raise ValueError("Invalid instrument_id.")

        if (
            not isinstance(instrument.symbol, str)
            or not instrument.symbol.strip()
        ):
            raise ValueError("Invalid symbol.")

        if (
            not isinstance(instrument.exchange, str)
            or not instrument.exchange.strip()
        ):
            raise ValueError("Invalid exchange.")

        if (
            not isinstance(instrument.asset, str)
            or not instrument.asset.strip()
        ):
            raise ValueError("Invalid asset.")

        if (
            not isinstance(instrument.name, str)
            or not instrument.name.strip()
        ):
            raise ValueError("Invalid name.")

        if not isinstance(
            instrument.instrument_type,
            InstrumentType,
        ):
            raise ValueError("Invalid instrument type.")

        if not isinstance(
            instrument.status,
            InstrumentStatus,
        ):
            raise ValueError("Invalid status.")

        if (
            not isinstance(instrument.currency, str)
            or not instrument.currency.strip()
        ):
            raise ValueError("Invalid currency.")

        if instrument.tick_size <= 0:
            raise ValueError("Invalid tick size.")

        if instrument.lot_size <= 0:
            raise ValueError("Invalid lot size.")

        if not isinstance(instrument.active, bool):
            raise ValueError("Invalid active flag.")

        if not isinstance(
            instrument.created_at,
            datetime,
        ):
            raise ValueError("Invalid created_at.")

        if not isinstance(
            instrument.updated_at,
            datetime,
        ):
            raise ValueError("Invalid updated_at.")

        return True