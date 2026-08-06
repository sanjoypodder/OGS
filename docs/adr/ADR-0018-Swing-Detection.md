# ADR-0018

## Title

Swing Detection Algorithm

## Status

Accepted

## Decision

The initial implementation of swing detection uses the Bill Williams five-candle fractal algorithm.

A candle is identified as:

- Swing High if its high is greater than the highs of the two preceding and two following candles.
- Swing Low if its low is lower than the lows of the two preceding and two following candles.

## Rationale

- Simple and deterministic.
- Widely used in technical analysis.
- Serves as a stable foundation for BOS, CHoCH, MSS, and liquidity analysis.

Future implementations (ATR-based, ZigZag, AI-assisted) will be added behind the same detector interface.