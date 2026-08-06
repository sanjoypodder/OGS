from ogs.market.symbol import AssetClass, Symbol


def test_symbol_value() -> None:
    assert Symbol.XAUUSD.value == "XAUUSD"


def test_asset_class() -> None:
    assert Symbol.XAUUSD.asset_class == AssetClass.METAL
    assert Symbol.BTCUSD.asset_class == AssetClass.CRYPTO
    assert Symbol.EURUSD.asset_class == AssetClass.FOREX


def test_forex_property() -> None:
    assert Symbol.EURUSD.is_forex is True
    assert Symbol.BTCUSD.is_forex is False


def test_crypto_property() -> None:
    assert Symbol.BTCUSD.is_crypto is True


def test_metal_property() -> None:
    assert Symbol.XAUUSD.is_metal is True


def test_index_property() -> None:
    assert Symbol.US30.is_index is True
