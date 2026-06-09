import os
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "IPTV Proxy Server is Live!"

# --- CHANNEL 1: Your original channel ---
@app.route('/playlist.m3u8')
def proxy_stream1():
    target_url = "http://tv-278956.ifiesta.net:8080/live/TV-13086383561888/231006460908/254477.m3u8?_lsr=mq3tkarw_m"
    return redirect(target_url, code=302)

# --- CHANNEL 2: Add a second stream here ---
@app.route('/sports.m3u8')
def proxy_stream2():
    # Replace the link below with your second stream URL
    target_url = "http://another-stream-link-here.com/live/stream.m3u8"
    return redirect(target_url, code=302)

# --- CHANNEL 3: Add a third stream here ---
@app.route('/news.m3u8')
def proxy_stream3():
    # Replace the link below with your third stream URL
    target_url = "http://a-third-stream-link-here.com/live/stream.m3u8"
    return redirect(target_url, code=302)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
