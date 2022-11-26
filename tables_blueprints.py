from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

table_blueprints = Blueprint('table_blueprints', __name__)
data_confing = load_file_config()
url_base = data_confing.get('http://127.0.0.1:8081') + "/table"


@table_blueprints.route("/table", methods=['GET'])
def get_all_students() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()
