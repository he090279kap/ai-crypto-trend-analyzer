from data_fetcher import get_crypto_data
from trend_analyzer import detect_trends
from price_predictor import predict_price
from telegram_bot import send_report

# Входные параметры
symbol = "BTC/USDT"
exchange = "binance"

# Получение данных
df = get_crypto_data(symbol, exchange)

# Анализ трендов
trend = detect_trends(df)

# Прогнозирование цен
predicted_price = predict_price(df)

# Отправка отчёта
report = f"📊 Анализ {symbol} на {exchange}\nТренд: {trend}\nПрогноз цены: {predicted_price:.2f} USDT"
send_report(report)

print("✅ Анализ завершён!")
