import pytest
import app # <--- Use the direct import

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, DevOps!" in response.data