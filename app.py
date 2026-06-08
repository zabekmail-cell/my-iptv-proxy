import os
from flask import Flask, redirect

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

# --- CHANNEL 3 ---
@app.route('/3/myplaylist_06062026.m3u8')
def proxy_stream3():
    target_url = "http://103.254.122.133/live/290113/24475A/1457488.m3u8?_t=1780862566426&_vnc=mq47lan4_l&token=SEReU0dfFg8WAAJVAgRVUgMLVAxXVlQPAVYBVVJQUQALVw8ADA8FBFEWGxRGRUZWVl9tXVAWWAgHVwAHCQtJFkYVU0BrXlAXDhYGAAUCAwoDEB4WQF0PXBFYBx8TQwxQEVwUAAIEDQMWGBVTTUVRQVlTXmtQURRQUAcVCV9GCVgfRFlca1NRWFVaUxQPEwQRGxBbR0QWWFdGDlsfE1EMQEEHQlcWDRYDBAEFFBkTV1xCXEZGTRZYG2MuFR8TVh1AVghFW1tZFg8WWQRDDRMYEV5BbUZRRxZLVgNaVkMRXxYDRBoQWVZMaldbWVhQUkBaWFxBFg4WUxsfQFpcX1oRW0E5RltQFQ4XBwMBAxcdFkZEV0BrXURAAxFVAB0HBksFA1cYAwMHFkg="
    return redirect(target_url, code=302)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
