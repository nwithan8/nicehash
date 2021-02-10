from datetime import datetime
from time import mktime
import uuid
import hmac
import json
from hashlib import sha256
from typing import Union


def resolution_converter(timeframe: str) -> str:
    if timeframe == "minute":
        return "1"
    elif timeframe == "hour":
        return "60"
    elif timeframe == "day":
        return "1440"
    return "60"


def filter_params(params: dict) -> dict:
    """
    Remove None or empty pairs from the param dicts

    :param params:
    :type params:
    :return:
    :rtype:
    """
    filtered_params = {}
    for k, v in params.items():
        if v:
            filtered_params[k] = v
    return filtered_params


def get_epoch_ms_from_now():
    now = datetime.now()
    now_ec_since_epoch = mktime(now.timetuple()) + now.microsecond / 1000000.0
    return int(now_ec_since_epoch * 1000)


def algo_settings_from_response(algorithm, algo_response):
    algo_setting = None
    for item in algo_response['miningAlgorithms']:
        if item['algorithm'] == algorithm:
            algo_setting = item

    if algo_setting is None:
        raise Exception('Settings for algorithm not found in algo_response parameter')

    return algo_setting


def get_encoded_header(api, method, path, query, body):
    xtime = get_epoch_ms_from_now()
    xnonce = str(uuid.uuid4())

    message = bytearray(api._key, 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(str(xtime), 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(xnonce, 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(api._organization, 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(method.upper(), 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(path, 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(query, 'utf-8')

    if body:
        body_json = json.dumps(body)
        message += bytearray('\x00', 'utf-8')
        message += bytearray(body_json, 'utf-8')

    digest = hmac.new(bytearray(api._secret, 'utf-8'), message, sha256).hexdigest()
    xauth = f"{api._key}:{digest}"

    headers = {
        'X-Time': str(xtime),
        'X-Nonce': xnonce,
        'X-Auth': xauth,
        'Content-Type': 'application/json',
        'X-Organization-Id': api._organization,
        'X-Request-Id': str(uuid.uuid4())
    }

    return headers
