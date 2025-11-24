import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    html = response.data.decode()

    assert "<h1>🍽️ My Food Blog</h1>" in html
    assert "Margherita Pizza" in html
    assert "Chocolate Cake" in html
    assert "Pasta Alfredo" in html
