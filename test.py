import pytest
from server import app as sanic_app


@pytest.fixture
def app():
    return sanic_app


def test_basic_test_client(app):
    request, response = app.test_client.get("/hello")

    assert request.method.lower() == "get"
    assert response.body == b"Hello, world."
    assert response.status == 200

    request, response = app.test_client.get("/hello")

    assert request.method.lower() == "get"
    assert response.body == b"Hello, world."
    assert response.status == 200
