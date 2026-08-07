"""
OGS Smart Money AI

Currency Analyzer
"""

from __future__ import annotations

from ogs.framework import BaseAnalyzer

from .collection import CurrencyCollection
from .statistics import CurrencyStatistics


class CurrencyAnalyzer(BaseAnalyzer):
    """
    Analyzer for Currency collections.

    Supports both the framework contract::

        CurrencyAnalyzer().analyze(collection)

    and the earlier bound-collection form::

        CurrencyAnalyzer(collection).analyze()
    """

    def __init__(
        self,
        collection: CurrencyCollection | None = None,
    ):
        self.collection = collection

    def _resolve_collection(
        self,
        collection: CurrencyCollection | None = None,
    ) -> CurrencyCollection:
        resolved = (
            collection
            if collection is not None
            else self.collection
        )

        if resolved is None:
            raise ValueError(
                "CurrencyCollection is required."
            )

        if not isinstance(resolved, CurrencyCollection):
            raise TypeError(
                "collection must be a CurrencyCollection"
            )

        return resolved

    def analyze(
        self,
        data: CurrencyCollection | None = None,
    ) -> dict:
        """
        Perform Currency analysis.
        """

        collection = self._resolve_collection(data)
        statistics = CurrencyStatistics(collection)

        return {
            "summary": statistics.summary(),
            "currency_analysis": {
                "count": statistics.count,
                "fiat_count": statistics.fiat_count,
                "crypto_count": statistics.crypto_count,
                "fiat_currencies": statistics.fiat_count,
                "crypto_currencies": statistics.crypto_count,
            },
            "distribution_analysis": {
                "currency_type": statistics.distribution(),
            },
        }

    def summary(
        self,
        collection: CurrencyCollection | None = None,
    ) -> dict:
        """Return Currency summary statistics."""

        resolved = self._resolve_collection(collection)

        return CurrencyStatistics(resolved).summary()

    def currency_analysis(
        self,
        collection: CurrencyCollection | None = None,
    ) -> dict:
        """Return core Currency statistics."""

        resolved = self._resolve_collection(collection)
        statistics = CurrencyStatistics(resolved)

        return {
            "count": statistics.count,
            "fiat_count": statistics.fiat_count,
            "crypto_count": statistics.crypto_count,
            "fiat_currencies": statistics.fiat_count,
            "crypto_currencies": statistics.crypto_count,
        }

    def distribution_analysis(
        self,
        collection: CurrencyCollection | None = None,
    ) -> dict:
        """Return Currency type distribution."""

        resolved = self._resolve_collection(collection)
        statistics = CurrencyStatistics(resolved)

        return {
            "currency_type": statistics.distribution(),
        }
