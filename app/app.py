from json import dumps
from flask import Flask, jsonify
from store_service import get_all_stores, get_store_by_id, get_store_by_district

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/v1/health", methods=["GET"])
def health():
    headers = {"Content-Type": "application/json"}
    return jsonify({"status": "ok"}), 200, headers


@app.route("/api/v1/store", methods=["GET"])
def all_stores():
    result = get_all_stores()
    headers = {"Content-Type": "application/json"}
    return jsonify({"result": result}), 200, headers


@app.route("/api/v1/store/<int:store_id>", methods=["GET"])
def store_by_id(store_id):
    result = get_store_by_id(store_id)
    headers = {"Content-Type": "application/json"}
    return jsonify({"result": result}), 200, headers


@app.route("/api/v1/store/district/<int:district>", methods=["GET"])
def store_by_district(district):
    result = get_store_by_district(district)
    headers = {"Content-Type": "application/json"}
    return jsonify({"result": result}), 200, headers
