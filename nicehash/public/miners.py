from nicehash.decorators import public_api_request


class Miners:
    def __init__(self, api):
        self._api = api

    @public_api_request
    def active_workers(self, bitcoin_address: str, size: int = 100, page: int = 0, sort_parameter: str = "RIG_NAME",
                       sort_direction: str = "ASC") -> dict:
        params = {
            "size": size,
            "page": page,
            "sortParameter": sort_parameter,
            "sortDirection": sort_direction
        }
        return "json", "get", f'/main/api/v2/mining/external/{bitcoin_address}/rigs/activeWorkers', params, None, False

    @public_api_request
    def stats(self, bitcoin_address: str, algorithm: str, after_timestamp: int = None,
              before_timestamp: int = None) -> dict:
        params = {
            "algorithm": algorithm,
            "afterTimestamp": after_timestamp,
            "beforeTimestamp": before_timestamp
        }
        return "json", "get", f'/main/api/v2/mining/external/{bitcoin_address}/rigs/stats/algo', params, None, False

    @public_api_request
    def unpaid(self, bitcoin_address: str, algorithm: str, after_timestamp: int = None,
               before_timestamp: int = None) -> dict:
        params = {
            "algorithm": algorithm,
            "afterTimestamp": after_timestamp,
            "beforeTimestamp": before_timestamp
        }
        return "json", "get", f'/main/api/v2/mining/external/{bitcoin_address}/rigs/stats/unpaid', params, None, False

    @public_api_request
    def withdrawals(self, bitcoin_address: str, after_timestamp: int = None, size: int = 100, page: int = 0) -> dict:
        params = {
            "afterTimestamp": after_timestamp,
            "size": size,
            "page": page
        }
        return "json", "get", f'/main/api/v2/mining/external/{bitcoin_address}/rigs/withdrawals', params, None, False

    @public_api_request
    def rigs(self, bitcoin_address: str, size: int = 100, page: int = 0, sort: str = "NAME") -> dict:
        params = {
            "size": size,
            "page": page,
            "sort": sort
        }
        return "json", "get", f'/main/api/v2/mining/external/{bitcoin_address}/rigs2', params, None, False
