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
    if not str(data.get("title", "")).strip():
        return jsonify({"error": "모임 이름을 입력하세요."}), 400
    try:
        max_members = int(data.get("max_members", 4))
    except (TypeError, ValueError):
        return jsonify({"error": "인원 수는 숫자로 입력하세요."}), 400
    study_id = db.create_study(
        str(data.get("title", "")),
        str(data.get("description", "")),
        str(data.get("place", "")),
        max_members,
    )
    return jsonify({"id": study_id}), 201


@app.get("/api/studies/<int:study_id>")
def get_study(study_id):
    study = db.get_study(study_id)
    if not study:
        return jsonify({"error": "모임을 찾을 수 없습니다."}), 404
    return jsonify(study)


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


@app.errorhandler(ValueError)
def handle_value_error(error):
    return jsonify({"error": str(error)}), 400


@app.errorhandler(404)
def handle_not_found(error):
    return jsonify({"error": "요청한 주소를 찾을 수 없습니다."}), 404


@app.errorhandler(500)
def handle_server_error(error):
    return jsonify({"error": "서버에서 문제가 생겼습니다. 잠시 후 다시 시도하세요."}), 500


if __name__ == "__main__":
    db.init_db()
    app.run(host="127.0.0.1", port=5000, debug=True)
