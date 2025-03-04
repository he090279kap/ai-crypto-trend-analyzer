import ccxt
import pandas as pd

def get_crypto_data(symbol, exchange="binance"):
    """Получает исторические данные криптовалюты."""
    ex = getattr(ccxt, exchange)()
    ohlcv = ex.fetch_ohlcv(symbol, timeframe="1d", limit=100)
    
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    
    return df
