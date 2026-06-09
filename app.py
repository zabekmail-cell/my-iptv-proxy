import os
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "IPTV Proxy Server is Live!"

@app.route('/playlist.m3u8')
def proxy_stream():
    # Your target token-protected live link
    target_url = "http://tv-278956.ifiesta.net:8080/live/TV-13086383561888/231006460908/254477.m3u8?_lsr=mq3tkarw_m"
    
    # 302 Redirect tells VLC to open the authenticated pipeline directly 
    # while inheriting the host handshake parameters.
    return redirect(target_url, code=302)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
