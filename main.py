from datetime import timedelta
from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, create_access_token)
from waitress import serve

import json
import requests

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "trabajofinal"
cors = CORS(app)
jwt = JWTManager(app)

HEADERS = {"Content-Type": "application/json; charset=utf-8"}


@app.route("/", methods=['GET'])
def home():
    response = {"message": "Welcome to the political API gateway G11...."}
    return response


@app.route("/login", methods=["POST"])
def login() -> tuple:
    user = request.get_json()
    url = data_config.get('url-backend-security') + "/user/login"
    response = requests.post(url, headers=HEADERS, json=user)
    if response.status_code == 200:
        user_logged = response.json()
        expires = timedelta(days=1)
        access_token = create_access_token(identity=user, expires_delta=expires)
        return {"token": access_token, "user_id": user_logged.get('id')},200
    else:
        return {"message": "Access denied"}, 401


# Config and execute app
def load_file_config():
    """
    Gets the data from the "config.json"
    :return:
    """
    with open("config.json", "r") as file_:
        data = json.load(file_)
    return data


if __name__ == '__main__':
    data_config = load_file_config()
    print("API gateway Server Running: http://" + data_config.get("url-api-gateway") + ":"
          + str(data_config.get("port")))
    serve(app, host=data_config.get("url-api-gateway"), port=data_config.get("port"))
