from flask import Flask, request
from messaging import send_daily_update
from env_config import settings
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Neuvaya WhatsApp Bot is live!"

@app.route('/send')
def trigger():
    key = request.args.get("key")
    if key != "changeme":
        return "Invalid key", 403
    send_daily_update()
    return "Message sent successfully!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 3000))  # Default to 3000 if PORT not set
    app.run(host="0.0.0.0", port=port)