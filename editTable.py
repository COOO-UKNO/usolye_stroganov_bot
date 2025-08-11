from flask import Flask, request, send_from_directory, jsonify, Response
from functools import wraps
import pandas as pd
import os
import base64

app = Flask(__name__)

XLSX_PATH = './data.xlsx'

USERNAME = os.getenv('ADMIN_USERNAME')
PASSWORD = os.getenv('ADMIN_PASSWORD')

def check_auth(auth_header):
    if not auth_header or not auth_header.startswith("Basic "):
        return False
    encoded = auth_header.split(" ")[1]
    decoded = base64.b64decode(encoded).decode()
    user, pwd = decoded.split(":", 1)
    return user == USERNAME and pwd == PASSWORD


def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not check_auth(request.headers.get('Authorization')):
            return Response(status=401, headers={'WWW-Authenticate': 'Basic realm="Login Required"'})
        return f(*args, **kwargs)
    return decorated


@app.route("/")
@require_auth
def index():
    return send_from_directory("static", "index.html")


@app.route("/data")
@require_auth
def get_data():
    df = pd.read_excel(XLSX_PATH)
    df = df.fillna("")  # Заменяем NaN на пустую строку
    print(df.to_dict(orient="records"))
    return jsonify(df.to_dict(orient="records"))


@app.route("/data", methods=["POST"])
@require_auth
def save_data():
    data = request.get_json()
    df = pd.DataFrame(data)
    df.to_excel(XLSX_PATH, index=False)
    return jsonify({"status": "ok"})


@app.route("/static/<path:path>")
def static_files(path):
    return send_from_directory("static", path)


def start():
    app.run(port=8000)