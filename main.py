from data_fetcher import get_crypto_data
from trend_analyzer import detect_trends
from price_predictor import train_lstm_model, predict_future_price
from telegram_bot import send_report

# Входные параметры
symbol = "BTC/USDT"
exchange = "binance"

# Получение данных
df = get_crypto_data(symbol, exchange)

# Анализ трендов
trend = detect_trends(df)

# Обучение LSTM и прогноз цены
train_lstm_model(df)
predicted_price = predict_future_price(df)

# Отправка отчёта в Telegram
report = f"📊 Анализ {symbol} на {exchange}\nТренд: {trend}\nПрогнозируемая цена (LSTM): {predicted_price:.2f} USDT"
send_report(report)

print("✅ Анализ завершён!")
