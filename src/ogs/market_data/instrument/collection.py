"""
OGS Smart Money AI

Instrument Collection
"""

from __future__ import annotations

from ogs.framework import BaseCollection

from .domain import Instrument
from .enums import (
    InstrumentStatus,
    InstrumentType,
)


class InstrumentCollection(BaseCollection[Instrument]):
    """
    Collection of Instrument objects.
    """

    def __init__(self, items=None):
        super().__init__(items)

    @property
    def items(self) -> list[Instrument]:
        return self._items

    def add(
        self,
        instrument: Instrument,
    ) -> None:
        self.append(instrument)

    def find(
        self,
        instrument_id: str,
    ) -> Instrument | None:
        return next(
            (
                item
                for item in self
                if item.instrument_id == instrument_id
            ),
            None,
        )

    def active(self) -> list[Instrument]:
        return [
            item
            for item in self
            if item.status == InstrumentStatus.ACTIVE
        ]

    def inactive(self) -> list[Instrument]:
        return [
            item
            for item in self
            if item.status != InstrumentStatus.ACTIVE
        ]

    def equities(self) -> list[Instrument]:
        return [
            item
            for item in self
            if item.instrument_type == InstrumentType.EQUITY
        ]

    def crypto(self) -> list[Instrument]:
        return [
            item
            for item in self
            if item.instrument_type == InstrumentType.CRYPTO
        ]

    def forex(self) -> list[Instrument]:
        return [
            item
            for item in self
            if item.instrument_type == InstrumentType.FOREX
        ]

    def futures(self) -> list[Instrument]:
        return [
            item
            for item in self
            if item.instrument_type == InstrumentType.FUTURE
        ]

    def options(self) -> list[Instrument]:
        return [
            item
            for item in self
            if item.instrument_type == InstrumentType.OPTION
        ]

    def to_list(self) -> list[dict]:
        return [
            item.to_dict()
            for item in self
        ]