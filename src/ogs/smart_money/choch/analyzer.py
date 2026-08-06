"""
===========================================================

OGS Smart Money AI

CHOCH Analyzer

===========================================================
"""

from __future__ import annotations

from ogs.smart_money.base import BaseAnalyzer
from ogs.smart_money.bos import BOSSeries, BOSType

from .collection import CHOCHSeries
from .domain import CHOCH
from .enums import CHOCHType


class CHOCHAnalyzer(
    BaseAnalyzer[
        BOSSeries,
        CHOCHSeries,
    ]
):
    """
    Detect Change of Character events.
    """

    def analyze(
        self,
        series: BOSSeries,
    ) -> CHOCHSeries:

        if series is None:
            return CHOCHSeries([])

        if len(series) < 2:
            return CHOCHSeries([])

        choch_events: list[CHOCH] = []

        previous = series[0]

        for current in series[1:]:

            # Bearish BOS → Bullish BOS
            if (
                previous.bos_type == BOSType.BEARISH
                and current.bos_type == BOSType.BULLISH
            ):

                choch_events.append(
                    CHOCH(
                        candle=current.candle,
                        broken_bos=current,
                        choch_type=CHOCHType.BULLISH,
                    )
                )

            # Bullish BOS → Bearish BOS
            elif (
                previous.bos_type == BOSType.BULLISH
                and current.bos_type == BOSType.BEARISH
            ):

                choch_events.append(
                    CHOCH(
                        candle=current.candle,
                        broken_bos=current,
                        choch_type=CHOCHType.BEARISH,
                    )
                )

            previous = current

        return CHOCHSeries(choch_events)