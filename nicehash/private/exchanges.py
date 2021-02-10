from typing import Union

from nicehash.decorators import private_api_request

class Exchanges:
    def __init__(self, api):
        self._api = api

    @private_api_request
    def cancel_all_orders(self, market: str = None, side: str = None) -> dict:
        params = {
            "market": market,
            "side": side
        }
        return "json", "delete", '/exchange/api/v2/info/cancelAllOrders', params, None, False

    @property
    @private_api_request
    def fee_status(self) -> dict:
        return "json", "get", '/exchange/api/v2/info/fees/status', None, None, False

    @private_api_request
    def my_order(self, market: str, order_id: str) -> dict:
        params = {
            "market": market,
            "orderId": order_id
        }
        return "json", "get", '/exchange/api/v2/info/myOrder', params, None, False

    @private_api_request
    def my_orders(self, market: str, order_state: str = None, order_status: str = None, sort_direction: str = "ASC", limit: int = 25, timestamp: int = None) -> dict:
        params = {
            "market": market,
            "orderState": order_state,
            "orderStatus": order_status,
            "sortDirection": sort_direction,
            "limit": limit,
            "timestamp": timestamp
        }
        return "json", "get", '/exchange/api/v2/info/myOrders', params, None, False

    @private_api_request
    def my_trades(self, market: str, sort_direction: str = "ASC", limit: int = 25, timestamp: int = None) -> dict:
        params = {
            "market": market,
            "sortDirection": sort_direction,
            "limit": limit,
            "timestamp": timestamp
        }
        return "json", "get", '/exchange/api/v2/info/myTrades', params, None, False

    @private_api_request
    def order_trades(self, market: str, order_id: str, sort_direction: str = "ASC") -> dict:
        params = {
            "market": market,
            "orderId": order_id,
            "sortDirection": sort_direction,
        }
        return "json", "get", '/exchange/api/v2/info/orderTrades', params, None, False

    @private_api_request
    def order(self, market: str, side: str, type: str, quantity: Union[float, int], price: Union[float, int], min_sec_quantity: Union[float, int], sec_quantity: Union[float, int], min_quantity: Union[float, int]) -> dict:
        params = {
            "market": market,
            "side": side,
            "type": type,
            "quantity": quantity,
            "price": price,
            "minSecQuantity": min_sec_quantity,
            "secQuantity": sec_quantity,
            "minQuantity": min_quantity
        }
        return "json", "post", '/exchange/api/v2/order', params, None, False

    @private_api_request
    def cancel_order(self, market: str, order_id: str) -> dict:
        params = {
            "market": market,
            "orderId": order_id
        }
        return "json", "delete", '/exchange/api/v2/order', params, None, False