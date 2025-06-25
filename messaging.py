from twilio.rest import Client
from env_config import settings
import yfinance as yf

def fetch_trending_stocks():
    symbols = ["AAPL", "TSLA", "GOOGL"]
    stocks = []
    
    for symbol in symbols:
        try:
            stock = yf.Ticker(symbol)
            hist = stock.history(period="1d")
            if hist.empty:
                print(f"⚠️ No data for {symbol}")
                continue
            price = hist["Close"].iloc[-1]
            stocks.append({"symbol": symbol, "price": round(price, 2)})
        except Exception as e:
            print(f"❌ Error fetching {symbol}: {e}")

    return stocks

def send_daily_update():
    client = Client(settings.TWILIO_SID, settings.TWILIO_AUTH_TOKEN)

    stocks = fetch_trending_stocks()
    if not stocks:
        print("❌ No stocks available to send.")
        return

    message = "📈 Daily Stock Picks:\n"
    for stock in stocks:
        message += f"- {stock['symbol']}: ${stock['price']}\n"

    try:
        msg = client.messages.create(
            body=message,
            from_=settings.FROM_WA,
            to=settings.TO_WA
        )
        print(f"✅ WhatsApp message sent! SID: {msg.sid}")
    except Exception as e:
        print(f"❌ Error sending WhatsApp message: {e}")