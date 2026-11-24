from flask import Flask, jsonify

from database import get_users

app = Flask(__name__)


@app.route("/api/users/names", methods=["GET"])
def api_get_user_names():
    return jsonify([user["name"] for user in get_users()]), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
