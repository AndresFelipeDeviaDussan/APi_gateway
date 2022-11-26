from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

results_blueprints = Blueprint('results_blueprints', __name__)
data_confing = load_file_config()
url_base = data_confing.get('url_backend-academic') + "/results"


@results_blueprints.route("/results", methods=['GET'])
def get_all_results() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@results_blueprints.route("/results/<string:id_>", methods=['GET'])
def get_results_by_id(id_: str) -> dict:
    url = url_base + f'/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@results_blueprints.route("/results/insert", methods=['POST'])
def insert_results() -> dict:
    results = request.get_json()
    url = url_base + "/insert"
    response = requests.post(url, headers=HEADERS, json=results)
    return response.json()


@results_blueprints.route("/results/update/<string:id_>", methods=['PUT'])
def update_results(id_: str) -> dict:
    results = request.get_json()
    url = url_base + f'/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=results)
    return  response.json()


@results_blueprints.route("/results/delete/<string:id_>", methods=['DELETE'])
def delete_results(id_: str) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()