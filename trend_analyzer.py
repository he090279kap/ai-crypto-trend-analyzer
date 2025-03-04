import pandas as pd

def detect_trends(df):
    """Определяет рыночный тренд на основе скользящих средних."""
    df["SMA_50"] = df["close"].rolling(window=50).mean()
    df["SMA_200"] = df["close"].rolling(window=200).mean()
    
    if df["SMA_50"].iloc[-1] > df["SMA_200"].iloc[-1]:
        return "📈 Бычий тренд (возможен рост)"
    else:
        return "📉 Медвежий тренд (возможен спад)"
