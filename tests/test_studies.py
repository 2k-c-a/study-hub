import pytest

import app as app_module
import db


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "test.db")
    db.init_db()
    app_module.app.config["TESTING"] = True
    return app_module.app.test_client()


def test_create_and_list(client):
    res = client.post("/api/studies", json={"title": "알고리즘 스터디", "place": "도서관", "max_members": 5})
    assert res.status_code == 201
    studies = client.get("/api/studies").get_json()
    assert [s["title"] for s in studies] == ["알고리즘 스터디"]


def test_delete(client):
    study_id = client.post("/api/studies", json={"title": "영어 회화"}).get_json()["id"]
    assert client.delete(f"/api/studies/{study_id}").status_code == 204
    assert client.get("/api/studies").get_json() == []
