from nicehash.decorators import private_api_request
import nicehash.utils as utils


class Pools:
    def __init__(self, api):
        self._api = api

    @private_api_request
    def create_pool(self, name: str, algorithm: str, pool_host: str, pool_port: int, username: str, password: str,
                    status: str = None, updated_timestamp: str = None, in_moratorium: bool = None) -> dict:
        data = {
            "name": name,
            "algorithm": algorithm,
            "stratumHostname": pool_host,
            "stratumPort": pool_port,
            "username": username,
            "password": password,
            "status": status,
            "updatedTs": updated_timestamp,
            "inMoratorium": in_moratorium
        }
        data = utils.filter_params(params=data)
        data['id'] = ""
        return "json", "post", '/main/api/v2/pool', None, data, True

    @private_api_request
    def pool_details(self, pool_id: str) -> dict:
        return "json", "get", f'/main/api/v2/pool/{pool_id}', None, None, False

    @private_api_request
    def delete_pool(self, pool_id: str) -> dict:
        return "json", "delete", f'/main/api/v2/pool/{pool_id}', None, None, False

    @private_api_request
    def pools(self, size: int = 100, page: int = 0, algorithm: str = None) -> dict:
        params = {
            "size": size,
            "page": page,
            "algorithm": algorithm
        }
        return "json", "get", '/main/api/v2/pools', params, None, False

    @private_api_request
    def verify_pool(self, verification_service_location: str, mining_algorithm: str, pool_host: str, pool_port: int, username: str, password: str) -> dict:
        data = {
            "poolVerificationServiceLocation": verification_service_location,
            "miningAlgorithm": mining_algorithm,
            "stratumHost": pool_host,
            "stratumPort": pool_port,
            "username": username,
            "password": password
        }
        return "json", "post", '/main/api/v2/pools/verify', None, data, False
