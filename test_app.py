import app

def test_home():
    client = "C:/Users/91866/Documents/ci-cd-flask/app.py".test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, DevOps!" in response.data