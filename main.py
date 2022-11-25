from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import (JWTManager)
from waitress import serve

import json

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "trabajofinal"
cors = CORS(app)
jwt = JWTManager(app)


@app.route("/", methods=['GET'])
def home():
    response = {"message": "Welcome to the political API gateway G11...."}
    return response


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
