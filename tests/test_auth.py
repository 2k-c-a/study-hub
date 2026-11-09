import pytest

import app as app_module
import db


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "test.db")
    db.init_db()
    app_module.app.config["TESTING"] = True
    return app_module.app.test_client()


def test_signup_and_login(client):
    assert client.post("/api/signup", json={"username": "doyoung", "password": "pw1234"}).status_code == 201
    res = client.post("/api/login", json={"username": "doyoung", "password": "pw1234"})
    assert res.status_code == 200
    assert res.get_json()["username"] == "doyoung"


def test_wrong_password(client):
    client.post("/api/signup", json={"username": "doyoung", "password": "pw1234"})
    res = client.post("/api/login", json={"username": "doyoung", "password": "wrong"})
    assert res.status_code == 401
