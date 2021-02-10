from typing import Union

from nicehash.decorators import public_api_request
import nicehash.validation as validation


class Hashpower:
    def __init__(self, api):
        self._api = api

    @public_api_request
    def orderbook(self, algorithm: str, size: int = 100, page: int = 0) -> dict:
        params = {
            "algorithm": algorithm,
            "page": page,
            "size": size
        }
        return "json", "get", '/main/api/v2/hashpower/orderBook', params, None, False

    @public_api_request
    def fixed_price(self, algorithm: str, market: str, limit: Union[float, int]) -> dict:
        body = {
            "algorithm": algorithm,
            "market": market,
            "limit": limit
        }
        validation.validate_dict(items=body)
        return "json", "post", '/main/api/v2/hashpower/orders/fixedPrice', None, body, True

    @public_api_request
    def summaries(self, market: str = None, algorithm: str = None) -> dict:
        params = {
            "market": market,
            "algorithm": algorithm
        }
        return "json", "get", '/main/api/v2/hashpower/orders/summaries', params, None, False

    @public_api_request
    def summary(self, market: str, algorithm: str) -> dict:
        params = {
            "market": market,
            "algorithm": algorithm
        }
        return "json", "get", '/main/api/v2/hashpower/orders/summary', params, None, False

    @public_api_request
    def history(self, algorithm: str) -> dict:
        params = {
            "algorithm": algorithm
        }
        return "json", "get", '/main/api/v2/public/algo/history', params, None, False

    @property
    @public_api_request
    def buy_info(self) -> dict:
        return "json", "get", '/main/api/v2/public/buy/info', None, None, False

    @public_api_request
    def orders(self, market: str = None, algorithm: str = None, operator: str = None, timestamp: int = None, page: int = 0,
               size: int = 100) -> dict:
        params = {
            "market": market,
            "algorithm": algorithm,
            "op": operator,
            "timestamp": timestamp,
            "page": page,
            "size": size
        }
        return "json", "get", '/main/api/v2/public/orders', params, None, False

    @property
    @public_api_request
    def simple_status(self) -> dict:
        return "json", "get", '/main/api/v2/public/simplemultialgo/info', None, None, False

    @property
    @public_api_request
    def global_stats_24h(self) -> dict:
        return "json", "get", '/main/api/v2/public/stats/global/24h', None, None, False

    @property
    @public_api_request
    def global_stats_current(self) -> dict:
        return "json", "get", '/main/api/v2/public/stats/global/current', None, None, False
