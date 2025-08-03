from flask import Flask, jsonify, request, redirect, abort
from .models import save_url, get_url, increment_click, get_stats, all_codes
from .utils import is_valid_url, generate_short_code

app = Flask(__name__)

@app.route('/')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "URL Shortener API"
    })

@app.route('/api/health')
def api_health():
    return jsonify({
        "status": "ok",
        "message": "URL Shortener API is running"
    })

@app.route('/api/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    if not data or 'url' not in data or not isinstance(data['url'], str):
        return jsonify({"error": "Missing or invalid URL"}), 400
    url = data['url'].strip()
    if not is_valid_url(url):
        return jsonify({"error": "Invalid URL"}), 400

    code = generate_short_code(all_codes())
    save_url(code, url)
    short_url = request.host_url.rstrip('/') + '/' + code
    return jsonify({"short_code": code, "short_url": short_url}), 201

@app.route('/<short_code>')
def redirect_short(short_code):
    entry = get_url(short_code)
    if not entry:
        abort(404)
    increment_click(short_code)
    return redirect(entry['url'])

@app.route('/api/stats/<short_code>')
def stats(short_code):
    entry = get_stats(short_code)
    if not entry:
        abort(404)
    return jsonify({
        "url": entry["url"],
        "clicks": entry["clicks"],
        "created_at": entry["created_at"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
