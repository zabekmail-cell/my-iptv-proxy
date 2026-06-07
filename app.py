import os
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "IPTV Proxy Server is Live!"

# --- CHANNEL 1 ---
@app.route('/1/myplaylist_06062026.m3u8')
def proxy_stream1():
    target_url = "http://tv-278956.ifiesta.net:8080/live/TV-13086383561888/231006460908/254477.m3u8?_lsr=mq3tkarw_m"
    return redirect(target_url, code=302)

# --- CHANNEL 2 ---
@app.route('/2/myplaylist_06062026.m3u8')
def proxy_stream2():
    target_url = "http://tv-278956.ifiesta.net:8080/live/TV-13086383561888/231006460908/254476.m3u8?_lsr=mq415z6j_3p1&_vnc=mq415z6k_3p2"
    return redirect(target_url, code=302)

# --- CHANNEL 3 ---
@app.route('/3/myplaylist_06062026.m3u8')
def proxy_stream3():
    target_url = "http://benchoda.xyz:8880/live/neil.woodward12/bjwseZ8JkH/4098190.m3u8?_lsr=mq425ppx_2"
    return redirect(target_url, code=302)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
