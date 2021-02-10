from nicehash.decorators import private_api_request


class Miners:
    def __init__(self, api):
        self._api = api

    @private_api_request
    def rigs(self, path: str = None, sort: str = "NAME", system: str = None, status: str = None, size: int = 25,
             page: int = 0) -> dict:
        params = {
            "size": size,
            "page": page,
            "path": path,
            "sort": sort,
            "system": system,
            "status": status
        }
        return "json", "get", '/main/api/v2/mining/rigs2', params, None, False

    @private_api_request
    def groups(self, extended_response: bool = False) -> dict:
        params = {
            "extendedResponse": extended_response
        }
        return "json", "get", '/main/api/v2/mining/groups/list', params, None, False

    @private_api_request
    def rig_stats(self, rig_id: str, algorithm: int, after_timestamp: int = None, before_timestamp: int = None) -> dict:
        params = {
            "rigId": rig_id,
            "algorithm": algorithm,
            "afterTimestamp": after_timestamp,
            "beforeTimestamp": before_timestamp
        }
        return "json", "get", '/main/api/v2/mining/rig/stats/algo', params, None, False

    @private_api_request
    def all_stats(self, algorithm: int, after_timestamp: int = None, before_timestamp: int = None) -> dict:
        params = {
            "algorithm": algorithm,
            "afterTimestamp": after_timestamp,
            "beforeTimestamp": before_timestamp
        }
        return "json", "get", '/main/api/v2/mining/rigs/stats/algo', params, None, False

    @private_api_request
    def rig_unpaid(self, rig_id: str, after_timestamp: int = None, before_timestamp: int = None) -> dict:
        params = {
            "rigId": rig_id,
            "afterTimestamp": after_timestamp,
            "beforeTimestamp": before_timestamp
        }
        return "json", "get", '/main/api/v2/mining/rig/stats/unpaid', params, None, False

    @private_api_request
    def all_unpaid(self, after_timestamp: int = None, before_timestamp: int = None) -> dict:
        params = {
            "afterTimestamp": after_timestamp,
            "beforeTimestamp": before_timestamp
        }
        return "json", "get", '/main/api/v2/mining/rigs/stats/unpaid', params, None, False

    @private_api_request
    def details(self, rig_id: str) -> dict:
        return "json", "get", f'/main/api/v2/mining/rig2/{rig_id}', None, None, False

    @private_api_request
    def active_workers(self, sort_parameter: str = "RIG_NAME", sort_direction: str = "ASC", size: int = 100,
                       page: int = 0) -> dict:
        params = {
            "size": size,
            "page": page,
            "sortParameter": sort_parameter,
            "sortDirection": sort_direction
        }
        return "json", "get", '/main/api/v2/mining/rigs/activeWorkers', params, None, False

    @private_api_request
    def payouts(self, after_timestamp: int = None, size: int = 100, page: int = 0) -> dict:
        params = {
            "afterTimestamp": after_timestamp,
            "size": size,
            "page": page
        }
        return "json", "get", '/main/api/v2/mining/rigs/payouts', params, None, False

    @private_api_request
    def update_status(self, group: str = None, rig_id: str = None, device_id: str = None, action: str = None,
                      options: list = None) -> dict:
        params = {
            "group": group,
            "rigId": rig_id,
            "deviceId": device_id,
            "action": action,
            "options": options
        }
        return "json", "post", '/main/api/v2/mining/rigs/status2', params, None, False
