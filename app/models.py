import threading
from datetime import datetime

# Internal datastore and lock
_url_store = {}
_store_lock = threading.Lock()

def save_url(short_code, url):
    with _store_lock:
        _url_store[short_code] = {
            'url': url,
            'created_at': datetime.now().isoformat(),
            'clicks': 0
        }

def get_url(short_code):
    with _store_lock:
        return _url_store.get(short_code)

def increment_click(short_code):
    with _store_lock:
        if short_code in _url_store:
            _url_store[short_code]['clicks'] += 1
            return True
        return False

def get_stats(short_code):
    with _store_lock:
        return _url_store.get(short_code)

def all_codes():
    with _store_lock:
        return set(_url_store.keys())
