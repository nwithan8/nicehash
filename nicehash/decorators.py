from functools import wraps

import nicehash.api_requests as api_requests
import nicehash.utils as utils
import nicehash.validation as validation


def public_api_request(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> dict:
        return_type, method, endpoint, params, body, ignore_filter = func(self, *args, *kwargs)

        if params:
            if not ignore_filter:
                params = utils.filter_params(params=params)
            validation.validate_dict(items=params)

        url = api_requests.make_url(base=self._api._url, endpoint=endpoint)
        return api_requests.request_type(return_type=return_type, method=method, url=url, params=params, data=body, log=("info" if self._api._verbose else None), session=self._api._session)

    return wrapper


def private_api_request(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> dict:
        return_type, method, endpoint, params, body, ignore_filter = func(self, *args, *kwargs)

        if params:
            if not ignore_filter:
                params = utils.filter_params(params=params)
            validation.validate_dict(items=params)

        query = api_requests.encode_params(params=params)
        headers = utils.get_encoded_header(api=self._api, method=method, path=endpoint, query=query, body=body)
        self._api._session.headers = headers

        url = api_requests.make_url(base=self._api._url, endpoint=endpoint)
        if query:
            url += f"?{query}"
        return api_requests.request_type(return_type=return_type, method=method, url=url, params=None, data=body,
                                         headers=headers, log=("info" if self._api._verbose else None), session=self._api._session)

    return wrapper