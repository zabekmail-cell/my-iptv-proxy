import os
from flask import Flask, redirect  # Ensure redirect is imported correctly

app = Flask(__name__)

@app.route('/')
def home():
    return "IPTV Proxy Server is Live!"

# --- CHANNEL 1 (Test Channel) ---
@app.route('/1/playlist.m3u8')
def proxy_stream1():
    # A permanent, 100% active public stream to test your server
    target_url = "https://demo.unified-streaming.com/k8s/features/stable/video/tears-of-steel/tears-of-steel.ism/.m3u8"
    return redirect(target_url, code=302)

# --- CHANNEL 2 (Test Channel) ---
@app.route('/2/playlist.m3u8')
def proxy_stream2():
    # A second active public test stream 
    target_url = "https://playertest.longtailvideo.com/adaptive/bipbop/bipbop_all.m3u8"
    return redirect(target_url, code=302)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
