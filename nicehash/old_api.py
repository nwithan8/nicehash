from functools import wraps

import requests
import nicehash.api_requests as api_requests
import nicehash.utils as utils


def public_api_request(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> dict:
        return_type, method, endpoint, params, body = func(self, *args, *kwargs)
        url = api_requests.make_url(base=self._url, endpoint=endpoint)
        return api_requests.request_type(return_type=return_type, method=method, url=url, params=params, data=body, log=("info" if self._verbose else None))

    return wrapper


def private_api_request(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> dict:
        return_type, method, endpoint, params, body = func(self, *args, *kwargs)
        query = api_requests.encode_params(params=params)
        header = utils.get_encoded_header(api=self, method=method, path=endpoint, query=query, body=body)
        url = api_requests.make_url(base=self._url, endpoint=endpoint)
        return api_requests.request_type(return_type=return_type, method=method, url=url, params=params, data=body,
                                         headers=header, log=("info" if self._verbose else None))

    return wrapper


class PublicAPI:
    def __init__(self, host: str = "https://api2.nicehash.com", verbose: bool = False):
        self._url = host
        self._verbose = verbose

    @property
    @public_api_request
    def current_global_stats(self) -> dict:
        return 'json', 'get', '/main/api/v2/public/stats/global/current/', None, None

    @property
    @public_api_request
    def global_stats_24h(self) -> dict:
        return 'json', 'get', '/main/api/v2/public/stats/global/24h/', None, None

    @property
    @public_api_request
    def active_orders(self) -> dict:
        return 'json', 'get', '/main/api/v2/public/orders/active/', None, None

    @property
    @public_api_request
    def active_orders_2(self) -> dict:
        return 'json', 'get', '/main/api/v2/public/orders/active2/', None, None

    @property
    @public_api_request
    def buy_info(self) -> dict:
        return 'json', 'get', '/main/api/v2/public/buy/info/', None, None

    @property
    @public_api_request
    def algorithms(self) -> dict:
        return 'json', 'get', '/main/api/v2/mining/algorithms/', None, None

    @property
    @public_api_request
    def markets(self) -> dict:
        return 'json', 'get', '/main/api/v2/mining/markets/', None, None

    @property
    @public_api_request
    def currencies(self) -> dict:
        return 'json', 'get', '/main/api/v2/public/currencies/', None, None

    @property
    @public_api_request
    def multialgo_info(self) -> dict:
        return 'json', 'get', '/main/api/v2/public/simplemultialgo/info/', None, None

    @property
    @public_api_request
    def exchange_markets_info(self) -> dict:
        return 'json', 'get', '/exchange/api/v2/info/status/', None, None

    @public_api_request
    def exchange_trades(self, market: str) -> dict:
        params = {
            "market": market
        }
        return 'json', 'get', f'/exchange/api/v2/info/trades', params, None

    @public_api_request
    def candlesticks(self, market: str, from_s, to_s, resolution) -> dict:
        params = {
            "market": market,
            "from": from_s,
            "to": to_s,
            "resolution": resolution
        }
        return 'json', 'get', '/exchange/api/v2/candlesticks', params, None

    @public_api_request
    def exchange_orderbook(self, market: str, limit) -> dict:
        params = {
            "market": market,
            "limit": limit
        }
        return 'json', 'get', '/exchange/api/v2/orderbook', params, None


class PrivateAPI:
    def __init__(self,
                 api_key: str,
                 api_secret: str,
                 organization_id: str,
                 host: str = "https://api2.nicehash.com",
                 verbose: bool = False,
                 session: requests.Session = None):
        self._url = host
        self._organization = organization_id
        self._key = api_key
        self._secret = api_secret
        self._verbose = verbose
        self._public = PublicAPI(host=host)
        self._session = session if session else api_requests.make_session()

    @property
    def current_global_stats(self) -> dict:
        return self._public.current_global_stats

    @property
    def global_stats_24h(self) -> dict:
        return self._public.global_stats_24h

    @property
    def active_orders(self) -> dict:
        return self._public.active_orders

    @property
    def active_orders_2(self) -> dict:
        return self._public.active_orders_2

    @property
    def buy_info(self) -> dict:
        return self._public.buy_info

    @property
    def algorithms(self) -> dict:
        return self._public.algorithms

    @property
    def markets(self) -> dict:
        return self._public.markets

    @property
    def currencies(self) -> dict:
        return self._public.currencies

    @property
    def multialgo_info(self) -> dict:
        return self._public.multialgo_info

    @property
    def exchange_markets_info(self) -> dict:
        return self._public.exchange_markets_info

    def exchange_trades(self, market: str) -> dict:
        return self._public.exchange_trades(market=market)

    def candlesticks(self, market: str, from_s, to_s, resolution) -> dict:
        return self._public.candlesticks(market=market, from_s=from_s, to_s=to_s, resolution=resolution)

    def exchange_orderbook(self, market: str, limit) -> dict:
        return self._public.exchange_orderbook(market=market, limit=limit)

    @private_api_request
    def accounts(self, currency: str = None) -> dict:
        return 'json', 'get', f'/main/api/v2/accounting/accounts2/{currency if currency else ""}', None, None

    @private_api_request
    def withdrawal_addresses(self, currency: str, size, page) -> dict:
        params = {
            "currency": currency,
            "size": size,
            "page": page
        }
        return 'json', 'get', '/main/api/v2/accounting/withdrawalAddresses/', params, None

    @property
    @private_api_request
    def withdrawal_types(self) -> dict:
        return 'json', 'get', '/main/api/v2/accounting/withdrawalAddresses/types/', None, None

    @private_api_request
    def withdraw(self, address_id: str, amount, currency) -> bool:
        withdraw_data = {
            "withdrawalAddressId": address_id,
            "amount": amount,
            "currency": currency
        }
        return 'bool', 'post', '/main/api/v2/accounting/withdrawal/', None, withdraw_data

    @private_api_request
    def active_orders(self, algorithm, market, limit) -> dict:
        ts = utils.get_epoch_ms_from_now()
        params = {
            "algorithm": algorithm,
            "market": market,
            "ts": ts,
            "limit": limit,
            "op": "LT"
        }
        return "json", "get", '/main/api/v2/hashpower/myOrders', params, None

    @private_api_request
    def create_pool(self, name, algorithm, pool_host, pool_port, username, password) -> bool:
        data = {
            "name": name,
            "algorithm": algorithm,
            "stratumHostname": pool_host,
            "stratumPort": pool_port,
            "username": username,
            "password": password
        }
        return "bool", "post", '/main/api/v2/pool/', None, data

    @private_api_request
    def delete_pool(self, pool_id: str) -> bool:
        return "bool", "delete", f'/main/api/v2/pool/{pool_id}', None, None

    @property
    @private_api_request
    def pools(self) -> dict:
        return "json", "get", '/main/api/v2/pools/', None, None

    @private_api_request
    def hashpower_orderbook(self, algorithm) -> dict:
        params = {
            "algorithm": algorithm
        }
        return "json", "get", '/main/api/v2/hashpower/orderBook/', params, None

    @private_api_request
    def create_hashpower_order(self, market, type, algorithm, price, limit, amount, pool_id, algo_response) -> bool:
        algo_setting = utils.algo_settings_from_response(algorithm, algo_response)
        order_data = {
            "market": market,
            "algorithm": algorithm,
            "amount": amount,
            "price": price,
            "limit": limit,
            "poolId": pool_id,
            "type": type,
            "marketFactor": algo_setting['marketFactor'],
            "displayMarketFactor": algo_setting['displayMarketFactor']
        }
        return "bool", "post", '/main/api/v2/hashpower/order/', None, order_data

    @private_api_request
    def cancel_hashpower_order(self, order_id) -> bool:
        return "bool", "delete", f'/main/api/v2/hashpower/order/{order_id}', None, None

    @private_api_request
    def refill_hashpower_order(self, order_id, amount) -> bool:
        refill_data = {
            "amount": amount
        }
        return "bool", "post", f'/main/api/v2/hashpower/order/{order_id}/refill', None, refill_data

    @private_api_request
    def set_price_hashpower_order(self, order_id, price, algorithm, algo_response) -> bool:
        algo_setting = utils.algo_settings_from_response(algorithm, algo_response)
        price_data = {
            "price": price,
            "marketFactor": algo_setting['marketFactor'],
            "displayMarketFactor": algo_setting['displayMarketFactor']
        }
        return "bool", "post", f'/main/api/v2/hashpower/order/{order_id}/updatePriceAndLimit/', None, price_data

    @private_api_request
    def set_limit_hashpower_order(self, order_id, limit, algorithm, algo_response) -> bool:
        algo_setting = utils.algo_settings_from_response(algorithm, algo_response)
        limit_data = {
            "limit": limit,
            "marketFactor": algo_setting['marketFactor'],
            "displayMarketFactor": algo_setting['displayMarketFactor']
        }
        return "bool", "post", f'/main/api/v2/hashpower/order/{order_id}/updatePriceAndLimit/', None, limit_data

    @private_api_request
    def set_price_and_limit_hashpower_order(self, order_id, price, limit, algorithm, algo_response) -> bool:
        algo_setting = utils.algo_settings_from_response(algorithm, algo_response)
        price_data = {
            "price": price,
            "limit": limit,
            "marketFactor": algo_setting['marketFactor'],
            "displayMarketFactor": algo_setting['displayMarketFactor']
        }
        return "bool", "post", f'/main/api/v2/hashpower/order/{order_id}/updatePriceAndLimit/', None, price_data

    @private_api_request
    def exchange_orders(self, market) -> dict:
        params = {
            "market": market
        }
        return "json", "get", '/exchange/api/v2/myOrders', params, None

    @private_api_request
    def exchange_trades(self, market) -> dict:
        params = {
            "market": market
        }
        return "json", "get", '/exchange/api/v2/myTrades', params, None

    @private_api_request
    def create_exchange_limit_order(self, market, side, quantity, price) -> bool:
        params = {
            "market": market,
            "side": side,
            "type": "limit",
            "quantity": quantity,
            "price": price
        }
        return "bool", "post", '/exchange/api/v2/order', params, None

    @private_api_request
    def create_exchange_buy_market_order(self, market, quantity) -> bool:
        params = {
            "market": market,
            "side": "buy",
            "type": "market",
            "secQuantity": quantity
        }
        return "bool", "post", '/exchange/api/v2/order', params, None

    @private_api_request
    def create_exchange_sell_market_order(self, market, quantity) -> bool:
        params = {
            "market": market,
            "side": "sell",
            "type": "market",
            "quantity": quantity
        }
        return "bool", "post", '/exchange/api/v2/order', params, None

    @private_api_request
    def cancel_exchange_order(self, market, order_id) -> bool:
        params = {
            "market": market,
            "orderId": order_id
        }
        return "bool", "delete", '/exchange/api/v2/order', params, None
