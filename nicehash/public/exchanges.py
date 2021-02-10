from nicehash.decorators import public_api_request
import nicehash.utils as utils
import nicehash.validation as validation


class Exchanges:
    def __init__(self, api):
        self._api = api

    @property
    @public_api_request
    def info(self) -> dict:
        return 'json', 'get', '/exchange/api/v2/info/status/', None, None, False

    @property
    @public_api_request
    def prices(self) -> dict:
        return 'json', 'get', '/exchange/api/v2/info/prices/', None, None, False

    @property
    @public_api_request
    def stats(self) -> dict:
        return 'json', 'get', '/exchange/api/v2/info/marketStats/', None, None, False

    @public_api_request
    def candlesticks(self, market: str, from_seconds: int, to_seconds: int, resolution: str) -> dict:
        resolution = utils.resolution_converter(timeframe=resolution)
        params = {
            "market": market,
            "from": from_seconds,
            "to": to_seconds,
            "resolution": resolution
        }
        return 'json', 'get', '/exchange/api/v2/info/candlesticks', params, None, False

    @public_api_request
    def trades(self, market: str, sort_direction: str = "ASC", limit: int = 25, timestamp: int = None) -> dict:
        params = {
            "market": market,
            "limit": limit,
            "sortDirection": sort_direction,
            "timestamp": timestamp
        }
        return 'json', 'get', f'/exchange/api/v2/info/trades', params, None, False

    @public_api_request
    def orderbook(self, market: str, limit: int = 25) -> dict:
        params = {
            "market": market,
            "limit": limit
        }
        return 'json', 'get', '/exchange/api/v2/orderbook', params, None, False
