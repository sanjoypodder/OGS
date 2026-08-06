"""
===========================================================

OGS Smart Money AI

Market Structure Engine

===========================================================
"""

from __future__ import annotations

from ogs.market import CandleSeries

from ogs.smart_money.swing import SwingAnalyzer
from ogs.smart_money.bos import BOSAnalyzer
from ogs.smart_money.choch import CHOCHAnalyzer
from ogs.smart_money.mss import MSSAnalyzer

from .analysis import Analysis


class MarketStructureEngine:
    """
    Orchestrates the complete market structure pipeline.
    """

    def __init__(self):

        self._swing = SwingAnalyzer()
        self._bos = BOSAnalyzer()
        self._choch = CHOCHAnalyzer()
        self._mss = MSSAnalyzer()

    def analyze(
        self,
        candles: CandleSeries,
    ) -> Analysis:

        swings = self._swing.analyze(candles)

        bos = self._bos.analyze(
            (
                candles,
                swings,
            )
        )

        choch = self._choch.analyze(bos)

        mss = self._mss.analyze(choch)

        return Analysis(
            swings=swings,
            bos=bos,
            choch=choch,
            mss=mss,
        )