import os
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "IPTV Proxy Server is Live!"

# --- CHANNEL 1: ABC (Src 1) ---
@app.route('/1/playlist.m3u8')
def proxy_stream1():
    target_url = "http://websafety101.net:5050/live/JermaineTy264/pk5KG5HCub/509081.m3u8"
    return redirect(target_url, code=302)

# --- CHANNEL 2: ABC (Src 2) ---
@app.route('/2/playlist.m3u8')
def proxy_stream2():
    target_url = "http://line.fire-4k.cc/live/290113/24475A/1457496.m3u8?_lsr=mq47jrig_1"
    return redirect(target_url, code=302)

# --- CHANNEL 3: CBS (Dulo TV) ---
@app.route('/3/playlist.m3u8')
def proxy_stream3():
    target_url = "https://gotcha.dulo.tv/memfs/bbf679fc-bf77-4ac4-a988-b36195bd1e31_output_0.m3u8?session=E2gTMBcp4ZxGhwurNJKHav"
    return redirect(target_url, code=302)

# --- CHANNEL 4: CBS (Src 2) ---
@app.route('/4/playlist.m3u8')
def proxy_stream4():
    target_url = "http://103.254.122.129/live/290113/24475A/1457769.m3u8?_t=1780952700819&_vnc=mq5p9phk_26&token=SEReU0dfFg8WUQdQBgVWAlNTAVVSBAYKUQdWUVUDBwBRVgRXVwFWA1YWGxRGRUZWVl9tXVAWWAgHVwAEBwpJFkYVU0BrXlAXDhYGAAUCAwoDEB4WQF0PXBFYBx8TQwxQEVwUAQYFDAQWGBVTTUVRQVlTXmtQURRQUAcVCV9GCVgfRFlca1NRWFVaUxQPEwQRGxBbR0QWWFdGDlsfE1EMQEEHQlcWDRYCDAMVGhdSW0ZZRkBNFg5AaX9AGxFUSxFRXRVfXVoVDhdZB0IOFx0WWkRtQFFHQBBcUg9SQRMJRwQRShRfVU9rVltaWVNWRV1cWUEQDhYFQBURD1hdWEcKRmwWX1YWDRYEBQMBBhcdFkZEV0BrXURAAxFVAB0HBksFA1cYAwMHFkg%3D"
    return redirect(target_url, code=302)

# --- CHANNEL 5: NBC Channel 1 ---
@app.route('/5/playlist.m3u8')
def proxy_stream5():
    target_url = "http://103.254.122.107/live/290113/24475A/1651867.m3u8?_t=1780862754014&_vnc=mq47pvv4_p&token=SEReU0dfFg8WBQJXAQABBlEHVFBWBAALA1UOVVNWAQRQVQRXBg8HUFIWGxRGRUZWVl9tXVAWWAgFVwYLBwRJFkYVU0BrXlAXDhYGAAUCAwoDEB4WQF0PXBFYBx8TQwxQEVwUAAUOAQEWGBVTTUVRQVlTXmtQURRQUAcVCV9GCVgfRFlca1NRWFVaUxQPEwQRGxBbR0QWWFdGDlsfE1EMQEEHQlcWDRYGDAUAFBkTV1xCXEZGTRZYG2MuFR8TVh1AVghFW1tZFg8WWQRDDRMYEV5BbUZRRxZLVgNaVkMRXxYDRBoQWVZMaldbWVhQUkBaWFxBFg4WUxsfQFpcX1oRW0E5RltQFQ4XBQEDAwcTGBFCQVdGa10SGwlAAAQfBVAaAlYHHAUABBdJ"
    return redirect(target_url, code=302)

# --- CHANNEL 6: MSNOW ---
@app.route('/6/playlist.m3u8')
def proxy_stream6():
    target_url = "http://line.fire-4k.cc/live/290113/24475A/360778.m3u8?_lsr=mq47cxc0_3&_vnc=mq47cxc3_4"
    return redirect(target_url, code=302)

# --- CHANNEL 7: BeinSport US ---
@app.route('/7/playlist.m3u8')
def proxy_stream7():
    target_url = "http://line.fire-4k.cc/live/290113/24475A/362747.m3u8?_lsr=mq47wfb6_1e"
    return redirect(target_url, code=302)

# --- CHANNEL 8: Golf Channel (Src 1) ---
@app.route('/8/playlist.m3u8')
def proxy_stream8():
    target_url = "https://tvsen6.aynaott.com/golfchannel/index.m3u8"
    return redirect(target_url, code=302)

# --- CHANNEL 8b: Golf Channel (Src 2) ---
@app.route('/8b/playlist.m3u8')
def proxy_stream8b():
    target_url = "http://websafety101.net:5050/live/JermaineTy264/pk5KG5HCub/509111.m3u8?_t=1780860641978&_vnc=mq46g1qd_1"
    return redirect(target_url, code=302)

# --- CHANNEL 9: Sky Sports+ (Src 1) ---
@app.route('/9/playlist.m3u8')
def proxy_stream9():
    target_url = "http://tv-278956.ifiesta.net:8080/live/TV-13086383561888/231006460908/254476.m3u8?_lsr=mq415z6j_3p1&_vnc=mq415z6k_3p2"
    return redirect(target_url, code=302)

# --- CHANNEL 10: Sky Sports+ (Src 2) ---
@app.route('/10/playlist.m3u8')
def proxy_stream10():
    target_url = "http://181.233.126.179/live/play/Y1RneFdXTnZkazlSYmtaM1NYZGxSMXBKWmxrNWFXVXpXRUZxWW5kSE1ERk5hVnBRTjBGU1UyRXpORDA9/254477"
    return redirect(target_url, code=302)

# --- CHANNEL 11: Sky Sports Mix ---
@app.route('/11/playlist.m3u8')
def proxy_stream11():
    target_url = "http://6zirt9yx.otttv.pw/iptv/HEGN4VXXQQSYCA/9293/index.m3u8"
    return redirect(target_url, code=302)

# --- CHANNEL 12: Sky Sports Golf (Src 1) ---
@app.route('/12/playlist.m3u8')
def proxy_stream12():
    target_url = "http://benchoda.xyz:8880/live/neil.woodward12/bjwseZ8JkH/4098190.m3u8?_lsr=mq425ppx_2"
    return redirect(target_url, code=302)

# --- CHANNEL 13: Sky Sports Golf (Src 2) ---
@app.route('/13/playlist.m3u8')
def proxy_stream13():
    target_url = "https://xemzi.short.gy/2000009"
    return redirect(target_url, code=302)

# --- CHANNEL 14: Polsat Sport 1 ---
@app.route('/14/playlist.m3u8')
def proxy_stream14():
    target_url = "http://203.76.253.100/live/290113/24475A/105387.m3u8?token=SEReU0dfFg8WBVZUBQMEAAIFAAEFDFENUgNWV1MGUQMFVFRTUFEFUQ0WGxRGRUZWVl9tXVAWWAgDVwQLBh9HQUADRG1dUxYPFgUBBgYGDQcVHhBAXVkHGwlSGxFBWgEWCUQCBgMEBRcYFlJOQVRGXVZebVBRQgtaVkANXURfCRgRCVhtUFJZVFpQFQwXARYfFVtBRBYODExfDhsRU1oRRlISUxAOFQcEAwEVGhdSW0ZZRkBNFg5AaX9AGxFUSxFRXRVfXVoVDhdZB0IOFx0WWkRtQFFHQBBcUg9SQRMJRwQRShRfVU9rVltaWVNWRV1cWUEQDhYFQBURD1hdWEcKRmwWX1YWDRYEBQMBBhcdFkZEV0BrXURAAxFVAB0HBksFA1cYAwMHFkg%3D&_vnc=mq46sklu_1"
    return redirect(target_url, code=302)

# --- CHANNEL 15: Polsat Sport 2 ---
@app.route('/15/playlist.m3u8')
def proxy_stream15():
    target_url = "http://line.fire-4k.cc/live/290113/24475A/105399.m3u8?_lsr=mq46ty2q_p"
    return redirect(target_url, code=302)

# --- CHANNEL 16: Polsat Sport 3 ---
@app.route('/16/playlist.m3u8')
def proxy_stream16():
    target_url = "http://203.76.253.100/live/290113/24475A/105393.m3u8?_t=1780861337338&_vnc=mq46vd0w_s&token=SEReU0dfFg8WDQQEUwdRVQFTU1IHDFJdBFQCBldVUFcGAABRB1ZWU1YWGxRGRUZWVl9tXVAWWAgDVwQKAh9HQUADRG1dUxYPFgUBBgYGDQcVHhBAXVkHGwlSGxFBWgEWCUQCAw0OBhcYFlJOQVRGXVZebVBRQgtaVkANXURfCRgRCVhtUFJZVFpQFQwXARYfFVtBRBYODExfDhsRU1oRRlISUxAOFQcEBgYVGhdSW0ZZRkBNFg5AaX9AGxFUSxFRXRVfXVoVDhdZB0IOFx0WWkRtQFFHQBBcUg9SQRMJRwQRShRfVU9rVltaWVNWRV1cWUEQDhYFQBURD1hdWEcKRmwWX1YWDRYEAwIHDxcdFkZEV0BrXURAAxFVAB0HBksFA1cYAwMHFkg%3D"
    return redirect(target_url, code=302)

# --- CHANNEL 17: Polsat Sport Premium 1 ---
@app.route('/17/playlist.m3u8')
def proxy_stream17():
    target_url = "http://line.fire-4k.cc/live/290113/24475A/105529.m3u8?_lsr=mq46x6qq_1v"
    return redirect(target_url, code=302)

# --- CHANNEL 18: Polsat Sport Premium 2 ---
@app.route('/18/playlist.m3u8')
def proxy_stream18():
    target_url = "http://103.254.122.107/live/290113/24475A/105530.m3u8?_t=1780861485336&_vnc=mq46yk53_1y&token=SEReU0dfFg8WBlIDBAkGBlMEVwYHUARcVVQDVlUKVFEFBARWVwcEBlYWGxRGRUZWVl9tXVAWWAgDVwIAAR9HQUADRG1dUxYPFgUBBgYGDQcVHhBAXVkHGwlSGxFBWgEWCUQHAQAPBxcYFlJOQVRGXVZebVBRQgtaVkANXURfCRgRCVhtUFJZVFpQFQwXARYfFVtBRBYODExfDhsRU1oRRlISUxAOFQYNAgcVGhdSW0ZZRkBNFg5AaX9AGxFUSxFRXRVfXVoVDhdZB0IOFx0WWkRtQFFHQBBcUg9SQRMJRwQRShRfVU9rVltaWVNWRV1cWUEQDhYFQBURD1hdWEcKRmwWX1YWDRYCBAYPFBkTQUBSQG1dRBZYGwRVGQUEHVQEAkgHBQQVSQ%3D%3D"
    return redirect(target_url, code=302)

# --- CHANNEL 19: Polsat Sport Premium 3 ---
@app.route('/19/playlist.m3u8')
def proxy_stream19():
    target_url = "http://103.254.122.107/live/290113/24475A/105531.m3u8?token=SEReU0dfFg8WVwMAU1UBAAdXVA0NBlQKUgAPBgECBFAGVgZUAg8GBgcWGxRGRUZWVl9tXVAWWAgDVwIAAB9HQUADRG1dUxYPFgUBBgYGDQcVHhBAXVkHGwlSGxFBWgEWCUQDBAUHFhkWUU9CUENaUlttVlFCXQFcEVhZRl1fSRZcCGlWUVpVW1AWDRQFExgRXkFCFg5aF1VfThVRWEcXVUcDFAgWAAMAAxYbFFZeQV1DQEsWDhYydRFOFVZJRwBaQA9ZXBYNFlgHQQ8UGRNdQGhAV0dARgdYXgdFEQsRVRYfRFtTTGhXWlpaUlVBWFtdRBAIFgUWThteDVlaRVwXa0MPUhAOFQMFAA0VGhdER1ZFbVtEFg5ADgRMAQYfAlUFHVcBAhZK"
    return redirect(target_url, code=302)

# --- CHANNEL 20: Polsat Sport Premium 4 ---
@app.route('/20/playlist.m3u8')
def proxy_stream20():
    target_url = "http://line.fire-4k.cc/live/290113/24475A/105532.m3u8?_lsr=mq471uof_2l&_vnc=mq471uog_2m"
    return redirect(target_url, code=302)

# --- CHANNEL 21: Polsat Sport Premium 5 ---
@app.route('/21/playlist.m3u8')
def proxy_stream21():
    target_url = "http://line.fire-4k.cc/live/290113/24475A/105533.m3u8?_lsr=mq47327g_3f&_vnc=mq47327i_3g"
    return redirect(target_url, code=302)

# --- CHANNEL 22: Polsat Sport Premium 6 ---
@app.route('/22/playlist.m3u8')
def proxy_stream22():
    target_url = "http://line.fire-4k.cc/live/290113/24475A/105534.m3u8?_lsr=mq474q2j_3j&_vnc=mq474q2k_3k"
    return redirect(target_url, code=302)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
