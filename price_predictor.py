import numpy as np
from sklearn.linear_model import LinearRegression

def predict_price(df):
    """Прогнозирует будущую цену на основе линейной регрессии."""
    df["index"] = np.arange(len(df))
    
    model = LinearRegression()
    model.fit(df[["index"]], df["close"])
    
    next_day = [[len(df)]]
    return model.predict(next_day)[0]
