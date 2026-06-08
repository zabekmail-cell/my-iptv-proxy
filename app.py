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

# --- CHANNEL 3 (CBS WITH HEADERS) ---
@app.route('/3/myplaylist_06062026.m3u8')
def proxy_stream3():
    target_url = "http://103.254.122.129/live/290113/24475A/1457769.m3u8?_t=1780952700819&_vnc=mq5p9phk_26&token=SEReU0dfFg8WUQdQBgVWAlNTAVVSBAYKUQdWUVUDBwBRVgRXVwFWA1YWGxRGRUZWVl9tXVAWWAgHVwAEBwpJFkYVU0BrXlAXDhYGAAUCAwoDEB4WQF0PXBFYBx8TQwxQEVwUAQYFDAQWGBVTTUVRQVlTXmtQURRQUAcVCV9GCVgfRFlca1NRWFVaUxQPEwQRGxBbR0QWWFdGDlsfE1EMQEEHQlcWDRYCDAMVGhdSW0ZZRkBNFg5AaX9AGxFUSxFRXRVfXVoVDhdZB0IOFx0WWkRtQFFHQBBcUg9SQRMJRwQRShRfVU9rVltaWVNWRV1cWUEQDhYFQBURD1hdWEcKRmwWX1YWDRYEBQMBBhcdFkZEV0BrXURAAxFVAB0HBksFA1cYAwMHFkg%3D"
    
    # Create a proper 302 Redirect Response object
    response = Response("", status=302)
    
    # Send the application straight to the provider's URL
    response.headers['Location'] = target_url
    
    # Force the app to forward a fake browser identity to trick the IP Lock
    response.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    
    return response
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
