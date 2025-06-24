from twilio.rest import Client
from env_config import settings
import yfinance as yf

def fetch_trending_stocks():
    # Replace with actual trending logic or keep placeholders
    symbols = ["AAPL", "TSLA", "GOOGL"]
    stocks = []
    for symbol in symbols:
        stock = yf.Ticker(symbol)
        price = stock.history(period="1d")["Close"].iloc[-1]
        stocks.append({"symbol": symbol, "price": round(price, 2)})
    return stocks

def send_daily_update():
    client = Client(settings.TWILIO_SID, settings.TWILIO_AUTH_TOKEN)

    stocks = fetch_trending_stocks()
    message = "📈 Daily Stock Picks:\n"
    for stock in stocks:
        message += f"- {stock['symbol']}: ${stock['price']}\n"

    client.messages.create(
        body=message,
        from_=settings.FROM_WA,
        to=settings.TO_WA
    )