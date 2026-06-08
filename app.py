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
    target_url = "http://103.254.122.129/live/290113/24475A/1457769.m3u8?_t=1780952700819&_vnc=mq5p9phk_26&token=SEReU0dfFg8WUQdQBgVWAlNTAVVSBAYKUQdWUVUDBwBRVgRXVwFWA1YWGxRGRUZWVl9tXVAWWAgHVwAEBwpJFkYVU0BrXlAXDhYGAAUCAwoDEB4WQF0PXBFYBx8TQwxQEVwUAQYFDAQWGBVTTUVRQVlTXmtQURRQUAcVCV9GCVgfRFlca1NRWFVaUxQPEwQRGxBbR0QWWFdGDlsfE1EMQEEHQlcWDRYCDAMVGhdSW0ZZRkBNFg5AaX9AGxFUSxFRXRVfXVoVDhdZB0IOFx0WWkRtQFFHQBBcUg9SQRMJRwQRShRfVU9rVltaWVNWRV1cWUEQDhYFQBURD1hdWEcKRmwWX1YWDRYEBQMBBhcdFkZEV0BrXURAAxFVAB0HBksFA1cYAwMHFkg%3D"
    return redirect(target_url, code=302)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
