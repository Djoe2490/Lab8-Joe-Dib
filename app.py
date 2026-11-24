from flask import Flask, jsonify, request
from flask_cors import CORS

from database import (
    FIELDS, create_db_table, delete_user, get_user_by_id, get_users,
    insert_user, patch_user, update_user,
)

app = Flask(__name__)
CORS(app)
create_db_table()


def read_user(partial=False, include_id=False):
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or not data:
        return None, "Send a JSON object with user fields"
    allowed = set(FIELDS) | ({"user_id"} if include_id else set())
    if set(data) - allowed:
        return None, "Unknown user field"
    if not partial and any(field not in data for field in FIELDS):
        return None, "Required fields: name, email, phone, address, country"
    for field in FIELDS:
        if field in data and (not isinstance(data[field], str) or not data[field].strip()):
            return None, f"{field} must be a non-empty string"
    if include_id and (type(data.get("user_id")) is not int or data["user_id"] < 1):
        return None, "user_id must be a positive integer"
    return data, None


@app.route("/api/users", methods=["GET"])
def api_get_users():
    return jsonify(get_users())


@app.route("/api/users/<int:user_id>", methods=["GET"])
def api_get_user(user_id):
    user = get_user_by_id(user_id)
    if user is None:
        return jsonify(error="User not found"), 404
    return jsonify(user)


@app.route("/api/users/add", methods=["POST"])
def api_add_user():
    user, error = read_user()
    if error:
        return jsonify(error=error), 400
    return jsonify(insert_user(user)), 201


@app.route("/api/users/update", methods=["PUT"])
def api_update_user():
    user, error = read_user(include_id=True)
    if error:
        return jsonify(error=error), 400
    updated = update_user(user)
    if updated is None:
        return jsonify(error="User not found"), 404
    return jsonify(updated)


@app.route("/api/users/<int:user_id>", methods=["PATCH"])
def api_patch_user(user_id):
    changes, error = read_user(partial=True)
    if error:
        return jsonify(error=error), 400
    updated = patch_user(user_id, changes)
    if updated is None:
        return jsonify(error="User not found"), 404
    return jsonify(updated)


@app.route("/api/users/delete/<int:user_id>", methods=["DELETE"])
def api_delete_user(user_id):
    if not delete_user(user_id):
        return jsonify(error="User not found"), 404
    return jsonify(status="User deleted successfully")


@app.errorhandler(404)
def not_found(error):
    return jsonify(error="Not found"), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify(error="Method not allowed"), 405


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
