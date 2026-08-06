"""
OGS Smart Money AI

Instrument Factory
"""

from __future__ import annotations

from copy import deepcopy

from .domain import Instrument
from .enums import (
    InstrumentStatus,
    InstrumentType,
)


class InstrumentFactory:
    """
    Factory for Instrument objects.
    """

    @staticmethod
    def create(
        instrument_id: str,
        symbol: str,
        exchange: str,
        asset: str,
        name: str,
        **kwargs,
    ) -> Instrument:

        return Instrument(
            instrument_id=instrument_id,
            symbol=symbol,
            exchange=exchange,
            asset=asset,
            name=name,
            **kwargs,
        )

    @staticmethod
    def equity(
        instrument_id: str,
        symbol: str,
        exchange: str,
        asset: str,
        name: str,
        **kwargs,
    ) -> Instrument:

        return Instrument(
            instrument_id=instrument_id,
            symbol=symbol,
            exchange=exchange,
            asset=asset,
            name=name,
            instrument_type=InstrumentType.EQUITY,
            status=InstrumentStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def crypto(
        instrument_id: str,
        symbol: str,
        exchange: str,
        asset: str,
        name: str,
        **kwargs,
    ) -> Instrument:

        return Instrument(
            instrument_id=instrument_id,
            symbol=symbol,
            exchange=exchange,
            asset=asset,
            name=name,
            instrument_type=InstrumentType.CRYPTO,
            status=InstrumentStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def forex(
        instrument_id: str,
        symbol: str,
        exchange: str,
        asset: str,
        name: str,
        **kwargs,
    ) -> Instrument:

        return Instrument(
            instrument_id=instrument_id,
            symbol=symbol,
            exchange=exchange,
            asset=asset,
            name=name,
            instrument_type=InstrumentType.FOREX,
            status=InstrumentStatus.ACTIVE,
            **kwargs,
        )

    @staticmethod
    def clone(
        instrument: Instrument,
    ) -> Instrument:

        return deepcopy(instrument)