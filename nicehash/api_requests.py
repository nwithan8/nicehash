from typing import Union
from urllib.parse import urlencode

import requests

import nicehash.api_logging as logs


def make_session():
    return requests.Session()


def make_url(base: str, endpoint: str, suffix: str = "") -> str:
    if endpoint.startswith("/"):
        endpoint = endpoint[1:]
    return f"{base}/{endpoint}{suffix}"


def encode_params(params: dict = None) -> str:
    if params:
        return urlencode(params)
    return ""


def get(url: str,
        params: dict = None,
        headers: dict = None,
        timeout: int = 2,
        log: str = None,
        session: requests.Session = None,
        **kwargs) -> Union[requests.Response, None]:
    if params:
        url += f"?{urlencode(params)}"
    try:
        if session:
            res = session.get(url=url, headers=headers, timeout=timeout)
        else:
            res = requests.get(url=url, headers=headers, timeout=timeout)
        if log:
            logs.log(message=f"GET {url}", level=log)
            logs.log(message=f"Response: {res}", level=("error" if not res else log))
        return res
    except requests.exceptions.Timeout:
        return None


def post(url: str,
         params: dict = None,
         headers: dict = None,
         data: dict = None,
         files: dict = None,
         timeout: int = 2,
         log: str = None,
         session: requests.Session = None,
         **kwargs) -> Union[requests.Response, None]:
    if params:
        url += f"?{urlencode(params)}"
    try:
        if session:
            res = session.post(url=url, json=data, files=files, headers=headers, timeout=timeout)
        else:
            res = requests.post(url=url, json=data, files=files, headers=headers, timeout=timeout)
        if log:
            logs.log(message=f"POST {url}, Body: {data}", level=log)
            logs.log(message=f"Response: {res}", level=("error" if not res else log))
        return res
        # use json= rather than data= to convert single-quoted dict to double-quoted JSON
    except requests.exceptions.Timeout:
        return None


def put(url: str,
        params: dict = None,
        headers: dict = None,
        data: dict = None,
        timeout: int = 2,
        log: str = None,
        session: requests.Session = None,
        **kwargs) -> Union[requests.Response, None]:
    if params:
        url += f"?{urlencode(params)}"
    try:
        if session:
            res = session.put(url=url, json=data, headers=headers, timeout=timeout)
        else:
            res = requests.put(url=url, json=data, headers=headers, timeout=timeout)
        if log:
            logs.log(message=f"PUT {url}, Body: {data}", level=log)
            logs.log(message=f"Response: {res}", level=("error" if not res else log))
        return res
        # use json= rather than data= to convert single-quoted dict to double-quoted JSON
    except requests.exceptions.Timeout:
        return None


def delete(url: str,
           params: dict = None,
           headers: dict = None,
           data: dict = None,
           timeout: int = 2,
           log: str = None,
           session: requests.Session = None,
           **kwargs) -> Union[requests.Response, None]:
    if params:
        url += f"?{urlencode(params)}"
    try:
        if session:
            res = session.delete(url=url, json=data, headers=headers, timeout=timeout)
        else:
            res = requests.delete(url=url, json=data, headers=headers, timeout=timeout)
        if log:
            logs.log(message=f"DELETE {url}, Body: {data}", level=log)
            logs.log(message=f"Response: {res}", level=("error" if not res else log))
        return res
        # use json= rather than data= to convert single-quoted dict to double-quoted JSON
    except requests.exceptions.Timeout:
        return None


def request(method,
            url: str,
            params: dict = None,
            headers: dict = None,
            data: dict = None,
            files: dict = None,
            timeout: int = 2,
            log: str = None,
            session: requests.Session = None) -> requests.Response:
    return globals()[method](**locals())


def request_bool(method,
                 url: str,
                 params: dict = None,
                 headers: dict = None,
                 data: dict = None,
                 files: dict = None,
                 timeout: int = 2,
                 log: str = None,
                 session: requests.Session = None) -> bool:
    try:
        res = globals()[method](**locals())
        if res:
            return True
        return False
    except:
        raise Exception(f"{method} is an invalid method")


def request_json(method,
                 url: str,
                 params: dict = None,
                 headers: dict = None,
                 data: dict = None,
                 files: dict = None,
                 timeout: int = 2,
                 log: str = None,
                 session: requests.Session = None) -> dict:
    try:
        res = globals()[method](**locals())
        if res:
            return res.json()
        return {}
    except:
        raise Exception(f"{method} is an invalid method")


def request_type(return_type: str,
                 method,
                 url: str,
                 params: dict = None,
                 headers: dict = None,
                 data: dict = None,
                 files: dict = None,
                 timeout: int = 2,
                 log: str = None,
                 session: requests.Session = None):
    if return_type == "json":
        return request_json(method=method, url=url, params=params, headers=headers, data=data, files=files,
                            timeout=timeout, log=log, session=session)
    elif return_type == 'bool':
        return request_bool(method=method, url=url, params=params, headers=headers, data=data, files=files,
                            timeout=timeout, log=log, session=session)
    else:
        return request(method=method, url=url, params=params, headers=headers, data=data, files=files,
                       timeout=timeout, log=log, session=session)
