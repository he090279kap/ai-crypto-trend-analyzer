import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 1))
model = None

def train_lstm_model(df):
    """Обучает модель LSTM на исторических данных."""
    global model
    
    # Подготовка данных
    data = df["close"].values.reshape(-1, 1)
    data_scaled = scaler.fit_transform(data)
    
    X_train, y_train = [], []
    for i in range(50, len(data_scaled)):
        X_train.append(data_scaled[i-50:i, 0])
        y_train.append(data_scaled[i, 0])

    X_train, y_train = np.array(X_train), np.array(y_train)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

    # Создание модели
    model = Sequential([
        LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
        LSTM(units=50, return_sequences=False),
        Dense(units=25),
        Dense(units=1)
    ])

    model.compile(optimizer="adam", loss="mean_squared_error")
    model.fit(X_train, y_train, epochs=20, batch_size=16, verbose=1)

def predict_future_price(df):
    """Прогнозирует цену на следующий день."""
    global model
    
    if model is None:
        return None

    last_50_days = df["close"].values[-50:].reshape(-1, 1)
    last_50_days_scaled = scaler.transform(last_50_days)

    X_test = np.array([last_50_days_scaled])
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    predicted_price_scaled = model.predict(X_test)
    predicted_price = scaler.inverse_transform(predicted_price_scaled)

    return predicted_price[0, 0]
