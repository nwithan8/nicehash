from typing import Union

from nicehash.decorators import private_api_request


class Accounting:
    def __init__(self, api):
        self._api = api

    @private_api_request
    def balance(self, currency: str, extended_response: bool = False) -> dict:
        params = {
            "extendedResponse": extended_response
        }
        return "json", "get", f'/main/api/v2/accounting/account2/{currency}', params, None, False

    @private_api_request
    def balances(self, fiat: str = None, extended_response: bool = False) -> dict:
        params = {
            "fiat": fiat,
            "extendedResponse": extended_response
        }
        return "json", "get", f'/main/api/v2/accounting/account2', params, None, False

    @private_api_request
    def my_orders(self, currency: str, activity_type: str = None, timestamp: int = None, stage: str = "ALL",
                  limit: int = 10) -> dict:
        valid_activity_types = ["DEPOSIT", "WITHDRAWAL", "HASHPOWER", "MINING", "EXCHANGE", "UNPAID_MINING", "OTHER"]
        if activity_type and activity_type not in valid_activity_types:
            raise Exception(f"Valid activity_type options: {', '.join(valid_activity_types)}")
        params = {
            "type": activity_type,
            "timestamp": timestamp,
            "stage": stage,
            "limit": limit
        }
        return "json", "get", f'/main/api/v2/accounting/activity/{currency}', params, None, True

    @private_api_request
    def deposit_address(self, currency: str, wallet_type: str = None) -> dict:
        params = {
            "currency": currency,
            "walletType": wallet_type
        }
        return "json", "get", f'/main/api/v2/accounting/depositAddress', params, None, False

    @private_api_request
    def deposits(self, currency: str, statuses: list = None, operator: str = None, timestamp: int = None, page: int = 0,
                 size: int = 100) -> dict:
        params = {
            "statuses": statuses,
            "op": operator,
            "timestamp": timestamp,
            "page": page,
            "size": size
        }
        return "json", "get", f'/main/api/v2/accounting/deposits/{currency}', params, None, False

    @private_api_request
    def get_deposit(self, currency: str, deposit_id: str) -> dict:
        return "json", "get", f'/main/api/v2/accounting/deposits2/{currency}/{deposit_id}', None, None, False

    @private_api_request
    def exchange_trades(self, exchange_id: str, exchange_market: str) -> dict:
        params = {
            "exchangeMarket": exchange_market,
        }
        return "json", "get", f'/main/api/v2/accounting/exchange/{exchange_id}/trades', params, None, False

    @private_api_request
    def hashpower_transactions(self, order_id: str, limit: int = 100, timestamp: int = None) -> dict:
        params = {
            "limit": limit,
            "timestamp": timestamp
        }
        return "json", "get", f'/main/api/v2/accounting/hashpower/{order_id}/transactions', params, None, False

    @private_api_request
    def mining_payments(self, currency: str, timestamp: int = None, page: int = 0, size: int = 100) -> dict:
        params = {
            "timestamp": timestamp,
            "page": page,
            "size": size
        }
        return "json", "get", f'/main/api/v2/accounting/hashpowerEarnings/{currency}', params, None, False

    @private_api_request
    def transaction(self, currency: str, transaction_id: str) -> dict:
        return "json", "get", f'/main/api/v2/accounting/transaction/{currency}/{transaction_id}', None, None, False

    @private_api_request
    def transactions(self, currency: str, transaction_type: str = None, purposes: list = None, operator: str = None,
                     timestamp: str = None, page: int = 0, size: int = 100) -> dict:
        valid_transaction_types = ["DEPOSIT", "WITHDRAWAL", "MOVE"]
        if transaction_type and transaction_type not in valid_transaction_types:
            raise Exception(f"Valid transaction_type options: {', '.join(valid_transaction_types)}")
        params = {
            "type": transaction_type,
            "purposes": purposes,
            "op": operator,
            "timestamp": timestamp,
            "page": page,
            "size": size
        }
        return "json", "get", f'/main/api/v2/accounting/transactions/{currency}', params, None, True

    @private_api_request
    def withdraw(self, currency: str, amount: Union[float, int], withdrawal_address_id: str) -> dict:
        body = {
            "currency": currency,
            "amount": amount,
            "withdrawalAddressId": withdrawal_address_id
        }
        return "json", "post", f'/main/api/v2/accounting/withdrawal', None, body, False

    @private_api_request
    def cancel_withdrawal(self, currency: str, withdrawal_id: str) -> dict:
        return "json", "delete", f'/main/api/v2/accounting/withdrawal/{currency}/{withdrawal_id}', None, None, False

    @private_api_request
    def withdrawal(self, currency: str, withdrawal_id: str) -> dict:
        return "json", "get", f'/main/api/v2/accounting/withdrawal2/{currency}/{withdrawal_id}', None, None, False

    @private_api_request
    def withdrawal_address(self, withdrawal_address: str) -> dict:
        return "json", "get", f'/main/api/v2/accounting/withdrawalAddress/{withdrawal_address}', None, None, False

    @private_api_request
    def withdrawal_addresses(self, currency: str = None, address_type: str = None, size: int = 100,
                             page: int = 0) -> dict:
        valid_address_types = ["crypto", "fiat"]
        if address_type and address_type not in valid_address_types:
            raise Exception(f"Valid address_type options: {', '.join(valid_address_types)}")
        params = {
            "currency": currency,
            "type": address_type,
            "page": page,
            "size": size
        }
        return "json", "get", f'/main/api/v2/accounting/withdrawalAddresses', params, None, True

    @private_api_request
    def withdrawals(self, currency: str, statuses: list = None, operator: str = "LT", timestamp: int = None,
                    page: int = 0, size: int = 100) -> dict:
        params = {
            "statuses": statuses,
            "op": operator,
            "timestamp": timestamp,
            "page": page,
            "size": size
        }
        return "json", "get", f'/main/api/v2/accounting/withdrawals/{currency}', params, None, False
