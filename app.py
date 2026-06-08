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

# --- CHANNEL 3 (CBS - DULO TV PROXY) ---
@app.route('/3/myplaylist_06062026.m3u8')
def proxy_stream3():
    # The corrected full URL with https:// added to the front
    target_url = "https://pontos.phantemlis.top/premium52/tracks-v1a1/mono.m3u8?md5=C2G7HMbCGuei3aR8QOyjXg&expires=1780959296"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://mages.dulo.tv/',
        'Origin': 'https://mages.dulo.tv'
    }
    
    try:
        # 1. Render downloads the true CBS file using our browser trick
        r = requests.get(target_url, headers=headers, timeout=10)
        text_data = r.text
        
        # 2. Fix the relative video links so your app knows to pull them from dulo.tv
        base_url = "https://mages.dulo.tv/memfs/"
        rewritten_data = []
        
        for line in text_data.splitlines():
            # If the line points to a video chunk or sub-playlist and doesn't have http, attach the base URL
            if ('.ts' in line or '.m3u8' in line) and not line.startswith('http'):
                # Handle leading slashes if present
                if line.startswith('/'):
                    rewritten_data.append("https://mages.dulo.tv" + line)
                else:
                    rewritten_data.append(base_url + line)
            else:
                rewritten_data.append(line)
                
        final_m3u8 = "\n".join(rewritten_data)
        
        return Response(final_m3u8, content_type='application/x-mpegURL')
        
    except Exception as e:
        return f"Proxy Error: {str(e)}", 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
