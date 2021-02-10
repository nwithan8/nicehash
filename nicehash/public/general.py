from nicehash.decorators import public_api_request

class General:
    def __init__(self, api):
        self._api = api

    @property
    @public_api_request
    def algorithms(self) -> dict:
        return 'json', 'get', '/main/api/v2/mining/algorithms/', None, None, False

    @property
    @public_api_request
    def currencies(self) -> dict:
        return 'json', 'get', '/main/api/v2/public/currencies/', None, None, False

    @property
    @public_api_request
    def fee_rules(self) -> dict:
        return 'json', 'get', '/main/api/v2/public/service/fee/info/', None, None, False

    @property
    @public_api_request
    def countries(self) -> dict:
        return 'json', 'get', '/api/v2/enum/countries/', None, None, False

    @property
    @public_api_request
    def km_countries(self) -> dict:
        return 'json', 'get', '/api/v2/enum/kmCountries/', None, None, False

    @property
    @public_api_request
    def permissions(self) -> dict:
        return 'json', 'get', '/api/v2/enum/permissions/', None, None, False

    @property
    @public_api_request
    def xch_countries(self) -> dict:
        return 'json', 'get', '/api/v2/enum/xchCountries/', None, None, False

    @property
    @public_api_request
    def flags(self) -> dict:
        return 'json', 'get', '/api/v2/system/flags/', None, None, False

    @property
    @public_api_request
    def time(self) -> dict:
        return 'json', 'get', '/api/v2/time/', None, None, False
