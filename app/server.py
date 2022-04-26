from flask import Flask, jsonify, request
from flask_cors import CORS
from decouple import config

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


from app.services.store_service import (
    get_all_stores,
    get_store_by_id,
    get_store_by_district,
)

from app.services.user_service import (
    create_admin_account,
    login_user,
)

from app.services.forecast_service import get_forecast

app = Flask(__name__)

app.config['SECRET_KEY'] = config('SECRET_KEY')
jwt = JWTManager(app)

# TODO: add prod origin
CORS(app, origins='http://localhost:8080')


@app.route('/api/v1/health', methods=['GET'])
def health():
    headers = {'Content-Type': 'application/json'}
    return jsonify({'status': 'ok'}), 200, headers


@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = login_user(email, password)
    print(user)
    # if not user:
    #     return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


@app.route('/api/v1/store', methods=['GET'])
@jwt_required()
def all_stores():
    result = get_all_stores()
    headers = {'Content-Type': 'application/json'}
    return jsonify({'result': result}), 200, headers


@app.route('/api/v1/store/<int:store_id>', methods=['GET'])
def store_by_id(store_id):
    result = get_store_by_id(store_id)
    headers = {'Content-Type': 'application/json'}
    return jsonify({'result': result}), 200, headers


@app.route('/api/v1/store/district/<int:district>', methods=['GET'])
def store_by_district(district):
    result = get_store_by_district(district)
    headers = {'Content-Type': 'application/json'}
    return jsonify({'result': result}), 200, headers


@app.route('/api/v1/store/<int:store_id>/forecast', methods=['GET'])
def prediction_by_store_id(store_id):
    start_date = request.args['start_date']
    end_date = request.args['end_date']

    result = get_forecast(store_id, start_date, end_date)
    headers = {'Content-Type': 'application/json'}
    return jsonify({'result': result}), 200, headers


@app.route('/admin', methods=['POST'])
def create_admin():
    first_name = request.json.get("firstName", None)
    last_name = request.json.get("lastName", None)
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    result = create_admin_account(first_name, last_name, email, password)
    headers = {'Content-Type': 'application/json'}
    return jsonify({'result': result}), 200, headers
