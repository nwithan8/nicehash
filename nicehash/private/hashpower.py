from typing import Union

from nicehash.decorators import private_api_request
import nicehash.validation as validation


class Hashpower:
    def __init__(self, api):
        self._api = api

    @private_api_request
    def my_orders(self, timestamp: int, operator: str, limit: int, algorithm: str = None, status: str = None,
                  only_active: bool = False, market: str = None) -> dict:
        params = {
            "ts": timestamp,
            "op": operator,
            "limit": limit,
            "algorithm": algorithm,
            "status": status,
            "active": only_active,
            "market": market
        }
        return "json", "get", '/main/api/v2/hashpower/myOrders', params, None, False

    @private_api_request
    def new_order(self, market: str, algorithm: str, amount: Union[float, int], display_market_factor: str,
                  market_factor: Union[float, int], price: Union[float, int], pool_id: str, limit: Union[float, int],
                  order_type: str) -> dict:
        body = {
            "market": market,
            "algorithm": algorithm,
            "amount": amount,
            "displayMarketFactor": display_market_factor,
            "marketFactor": market_factor,
            "price": price,
            "poolId": pool_id,
            "limit": limit,
            "type": order_type
        }
        validation.validate_dict(items=body)
        return "json", "post", '/main/api/v2/hashpower/order', None, body, True

    @private_api_request
    def order_details(self, order_id: str) -> dict:
        return "json", "get", f'/main/api/v2/hashpower/order/{order_id}', None, None, False

    @private_api_request
    def cancel_order(self, order_id: str) -> dict:
        return "json", "delete", f'/main/api/v2/hashpower/order/{order_id}', None, None, False

    @private_api_request
    def refill_order(self, order_id: str, amount: Union[float, int]) -> dict:
        body = {
            "amount": amount
        }
        return "json", "post", f'/main/api/v2/hashpower/order/{order_id}/refill', None, body, False

    @private_api_request
    def order_stats(self, order_id: str, after_timestamp: int = None) -> dict:
        params = {
            "afterTimestamp": after_timestamp
        }
        return "json", "get", f'/main/api/v2/hashpower/order/{order_id}/stats', params, None, False

    @private_api_request
    def update_price_and_limit(self, order_id: str, price: Union[float, int], limit: Union[float, int],
                               display_market_factor: str, market_factor: Union[float, int]) -> dict:
        body = {
            "price": price,
            "limit": limit,
            "displayMarketFactor": display_market_factor,
            "marketFactor": market_factor
        }
        return "json", "post", f'/main/api/v2/hashpower/order/{order_id}/updatePriceAndLimit', None, body, False

    @private_api_request
    def estimate_order_duration(self, order_type: str, price: Union[float, int], limit: Union[float, int],
                                amount: Union[float, int], display_market_factor: str, market_factor: Union[float, int],
                                decrease_fee: bool = False) -> dict:
        body = {
            "type": order_type,
            "price": price,
            "limit": limit,
            "amount": amount,
            "decreaseFee": decrease_fee,
            "displayMarketFactor": display_market_factor,
            "marketFactor": market_factor
        }
        validation.validate_dict(items=body)
        return "json", "post", f'/main/api/v2/hashpower/orders/calculateEstimateDuration', None, body, False
