import os
from flask import Flask, redirect  # Ensure redirect is properly imported here

app = Flask(__name__)

@app.route('/')
def home():
    return "IPTV Proxy Server is Live!"

# --- CHANNEL 1 ---
@app.route('/1/playlist.m3u8')  # Moved into isolated folder 1
def proxy_stream1():
    target_url = "http://tv-278956.ifiesta.net:8080/live/TV-13086383561888/231006460908/254477.m3u8?_lsr=mq3tkarw_m"
    return redirect(target_url, code=302)

# --- CHANNEL 2 ---
@app.route('/2/playlist.m3u8')  # Moved into isolated folder 2
def proxy_stream2():
    target_url = "http://another-stream-link-here.com/live/stream.m3u8"
    return redirect(target_url, code=302)

# --- CHANNEL 3 ---
@app.route('/3/playlist.m3u8')  # Moved into isolated folder 3
def proxy_stream3():
    target_url = "http://a-third-stream-link-here.com/live/stream.m3u8"
    return redirect(target_url, code=302)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
