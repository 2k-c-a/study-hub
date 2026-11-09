from flask import Flask, jsonify, request, send_from_directory

import db

app = Flask(__name__, static_folder="static", static_url_path="")


@app.get("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.get("/api/studies")
def get_studies():
    return jsonify(db.list_studies())


@app.post("/api/studies")
def post_study():
    data = request.get_json(silent=True) or {}
    study_id = db.create_study(
        data.get("title", ""),
        data.get("description", ""),
        data.get("place", ""),
        int(data.get("max_members", 4)),
    )
    return jsonify({"id": study_id}), 201


@app.delete("/api/studies/<int:study_id>")
def remove_study(study_id):
    db.delete_study(study_id)
    return "", 204


@app.post("/api/signup")
def signup():
    data = request.get_json(silent=True) or {}
    username = data.get("username", "").strip()
    password = data.get("password", "")
    if not username or not password:
        return jsonify({"error": "아이디와 비밀번호를 입력하세요."}), 400
    db.create_user(username, password)
    return jsonify({"ok": True}), 201


@app.post("/api/login")
def login():
    data = request.get_json(silent=True) or {}
    user = db.find_user(data.get("username", ""), data.get("password", ""))
    if not user:
        return jsonify({"error": "아이디 또는 비밀번호가 맞지 않습니다."}), 401
    return jsonify({"ok": True, "username": user["username"]})


if __name__ == "__main__":
    db.init_db()
    app.run(host="127.0.0.1", port=5000, debug=True)
