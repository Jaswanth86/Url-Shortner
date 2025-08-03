import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['service'] == 'URL Shortener API'

def test_shorten_and_redirect(client):
    resp = client.post('/api/shorten', json={'url': 'https://www.google.com'})
    assert resp.status_code == 201
    data = resp.get_json()
    code = data['short_code']

    # Redirection
    resp2 = client.get(f'/{code}', follow_redirects=False)
    assert resp2.status_code == 302

    # Analytics: one hit!
    resp3 = client.get(f'/api/stats/{code}')
    assert resp3.status_code == 200
    stats = resp3.get_json()
    assert stats['clicks'] == 1
    assert stats['url'] == 'https://www.google.com'

def test_invalid_url(client):
    resp = client.post('/api/shorten', json={'url': 'notaurl'})
    assert resp.status_code == 400

def test_missing_url(client):
    resp = client.post('/api/shorten', json={})
    assert resp.status_code == 400

def test_not_found(client):
    assert client.get('/notrealcode').status_code == 404
    assert client.get('/api/stats/notrealcode').status_code == 404
