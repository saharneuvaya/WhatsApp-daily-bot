from flask import Flask, request
from messaging import send_daily_update
from env_config import settings

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