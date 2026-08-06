"""
===========================================================

OGS Smart Money AI

MSS Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseAnalyzer
from ogs.smart_money.choch import (
    CHOCHSeries,
    CHOCHType,
)

from .collection import MSSSeries
from .domain import MSS
from .enums import MSSType


class MSSAnalyzer(
    BaseAnalyzer[
        CHOCHSeries,
        MSSSeries,
    ]
):
    """
    Detect confirmed Market Structure Shift (MSS).

    Version 1:
    An MSS is created whenever the CHOCH direction reverses.
    """

    def analyze(
        self,
        series: CHOCHSeries,
    ) -> MSSSeries:

        if series is None:
            return MSSSeries([])

        if len(series) < 2:
            return MSSSeries([])

        mss_events: list[MSS] = []

        previous = series[0]

        for current in series[1:]:

            # Bearish CHOCH -> Bullish CHOCH
            if (
                previous.choch_type == CHOCHType.BEARISH
                and current.choch_type == CHOCHType.BULLISH
            ):

                mss_events.append(
                    MSS(
                        candle=current.candle,
                        triggering_choch=current,
                        mss_type=MSSType.BULLISH,
                    )
                )

            # Bullish CHOCH -> Bearish CHOCH
            elif (
                previous.choch_type == CHOCHType.BULLISH
                and current.choch_type == CHOCHType.BEARISH
            ):

                mss_events.append(
                    MSS(
                        candle=current.candle,
                        triggering_choch=current,
                        mss_type=MSSType.BEARISH,
                    )
                )

            previous = current

        return MSSSeries(mss_events)