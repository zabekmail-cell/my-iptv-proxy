import os
import requests  # Added missing import
from flask import Flask, redirect, Response  # Added missing Response import

app = Flask(__name__)

@app.route('/')
def home():
    return "IPTV Proxy Server is Live!"

# --- CHANNEL 1 ---
@app.route('/1/myplaylist_06062026.m3u8')
def proxy_stream1():
    target_url = "http://websafety101.net:5050/live/JermaineTy264/pk5KG5HCub/509081.m3u8"
    return redirect(target_url, code=302)

# --- CHANNEL 2 ---
@app.route('/2/myplaylist_06062026.m3u8')
def proxy_stream2():
    target_url = "http://line.fire-4k.cc/live/290113/24475A/1457496.m3u8?_lsr=mq47jrig_1"
    return redirect(target_url, code=302)

# --- CHANNEL 3 (CBS) ---
@app.route('/3/myplaylist_06062026.m3u8')
def proxy_stream3():
    target_url = "http://103.254.122.107/live/290113/24475A/1651867.m3u8?_t=1780862754014&_vnc=mq47pvv4_p&token=SEReU0dfFg8WBQJXAQABBlEHVFBWBAALA1UOVVNWAQRQVQRXBg8HUFIWGxRGRUZWVl9tXVAWWAgFVwYLBwRJFkYVU0BrXlAXDhYGAAUCAwoDEB4WQF0PXBFYBx8TQwxQEVwUAAUOAQEWGBVTTUVRQVlTXmtQURRQUAcVCV9GCVgfRFlca1NRWFVaUxQPEwQRGxBbR0QWWFdGDlsfE1EMQEEHQlcWDRYGDAUAFBkTV1xCXEZGTRZYG2MuFR8TVh1AVghFW1tZFg8WWQRDDRMYEV5BbUZRRxZLVgNaVkMRXxYDRBoQWVZMaldbWVhQUkBaWFxBFg4WUxsfQFpcX1oRW0E5RltQFQ4XBQEDAwcTGBFCQVdGa10SGwlAAAQfBVAaAlYHHAUABBdJ"
    return redirect(target_url, code=302)

# --- CHANNEL 4 ---
@app.route('/4/myplaylist_06062026.m3u8')  # Fixed route path from /2/ to /4/
def proxy_stream4():
    target_url = "http://103.254.122.107/live/290113/24475A/1457617.m3u8?_t=1780862852209&_vnc=mq47rvfz_13&token=SEReU0dfFg8WAgEHAQRVVQZQAwwMAVYLAVoHBFILAVBWUQ8EVwEEUAUWGxRGRUZWVl9tXVAWWAgHVwAFAARJFkYVU0BrXlAXDhYGAAUCAwoDEB4WQF0PXBFYBx8TQwxQEVwUAQwHDQMWGBVTTUVRQVlTXmtQURRQUAcVCV9GCVgfRFlca1NRWFVaUxQPEwQRGxBbR0QWWFdGDlsfE1EMQEEHQlcWDRYDAgAFFBkTV1xCXEZGTRZYG2MuFR8TVh1AVghFW1tZFg8WWQRDDRMYEV5BbUZRRxZLVgNaVkMRXxYDRBoQWVZMaldbWVhQUkBaWFxBFg4WUxsfQFpcX1oRW0E5RltQFQ4XBQcPAQYTGBFCQVdGa10SGwlAAAQfBVAaAlYHHAUABBdJ"
    return redirect(target_url, code=302)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
