import requests

import nicehash.api_requests as api_requests
import nicehash.public as public
import nicehash.private as private

class PublicAPI:
    def __init__(self, host: str = "https://api2.nicehash.com", verbose: bool = False, session: requests.Session = None):
        self._url = host
        self._verbose = verbose
        self._session = session if session else api_requests.make_session()

        self._exchanges = public.Exchanges(api=self)
        self._mining = public.Miners(api=self)
        self._hashpower = public.Hashpower(api=self)
        self._general = public.General(api=self)

    @property
    def Exchanges(self):
        return self._exchanges

    @property
    def Mining(self):
        return self._mining

    @property
    def Hashpower(self):
        return self._hashpower

    @property
    def General(self):
        return self._general

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
        self._session = session if session else api_requests.make_session()

        self._public = PublicAPI(host=host)

        self._accounting = private.Accounting(api=self)
        self._mining = private.Miners(api=self)
        self._pools = private.Pools(api=self)
        self._exchanges = private.Exchanges(api=self)
        self._hashpower = private.Hashpower(api=self)

    @property
    def Exchanges(self):
        return self._exchanges

    @property
    def Mining(self):
        return self._mining

    @property
    def Hashpower(self):
        return self._hashpower

    @property
    def Pools(self):
        return self._pools

    @property
    def Accounting(self):
        return self._accounting

    # Don't use this. Public methods routed automatically
    # Nah, nevermind
    @property
    def Public(self):
        return self._public

