import os
import urllib.request
from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def home():
    return "IPTV Proxy Server is Live!"

@app.route('/playlist.m3u8')
def proxy_stream():
    # Your target token-protected live link
    target_url = "http://line.fire-4k.cc/live/290113/24475A/1457496.m3u8?_lsr=mq47jrig_1"
    
    req = urllib.request.Request(
        target_url, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
            'Referer': 'http://ifiesta.net/',
            'Origin': 'http://ifiesta.net'
        }
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            return Response(response.read(), mimetype='application/x-mpegURL', headers={'Access-Control-Allow-Origin': '*'})
    except Exception as e:
        return f"Proxy Error: {str(e)}", 500

if __name__ == "__main__":
    # Render passes the port dynamically via an environment variable
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
