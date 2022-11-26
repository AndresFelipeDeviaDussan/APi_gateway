import json
import re

import requests

HEADERS = {"Content-Type": "application/json; charset=utf-8"}


def load_file_config():
    """
    Gets the data from the "config.json"
    :return:
    """
    with open("config.json", "r") as file_:
        data = json.load(file_)
    return data


def clear_url(url: str) -> str:
    """
    It is responsible for traversing the entire url in order to find numerical data to replace them with the symbol '?'
    with the objective of validating the user's permissions
    :param url:
    :return:
    """
    segments = url.split('/')
    for segments in segments:
        if re.search('\\d', segments):
            url = url.replace(segments, '?')
    return url


def validate_grant(endpoints: str, methods: str, id_rol: str):
    """
    Validate permission
    :param endpoints:
    :param methods:
    :param id_rol:
    :return:
    """
    data_confing = load_file_config()
    url = data_confing.get('url-backend-security') + f'/rol/validate/{id_rol}'  # The 'f' is to concatenate the str
    body = {
        "url": endpoints,
        "methods": methods
    }
    response = requests.get(url, headers=HEADERS, json=body)
    has_grant = False
    try:
        if response.status_code == 200:
            has_grant = True
    except Exception as e:
        print(e)
    return has_grant
