from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

political_parties_blueprints = Blueprint('political_parties_blueprints', __name__)
data_confing = load_file_config()
url_base = data_confing.get('url_backend-academic') + "/political_parties"


@political_parties_blueprints.route("/political_parties", methods=['GET'])
def get_all_political_parties() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@political_parties_blueprints.route("/political_parties/<string:id_>", methods=['GET'])
def get_political_parties_by_id(id_: str) -> dict:
    url = url_base + f'/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@political_parties_blueprints.route("/political_parties/insert", methods=['POST'])
def insert_political_parties() -> dict:
    political_parties = request.get_json()
    url = url_base + "/insert"
    response = requests.post(url, headers=HEADERS, json=political_parties)
    return response.json()


@political_parties_blueprints.route("/political_parties/update/<string:id_>", methods=['PUT'])
def update_political_parties(id_: str) -> dict:
    political_parties = request.get_json()
    url = url_base + f'/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=political_parties)
    return  response.json()


@political_parties_blueprints.route("/political_parties/delete/<string:id_>", methods=['DELETE'])
def delete_political_parties(id_: str) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()