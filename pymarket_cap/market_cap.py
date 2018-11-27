import requests

from .exceptions import *


class CoinMarketCap:
    PRODUCTION_BASE_URL = 'https://pro-api.coinmarketcap.com'
    SANDBOX_BASE_URL = 'https://sandbox-api.coinmarketcap.com'

    def __init__(self, api_key, version='v1', is_sandbox=True, fetch_timeout=None):
        self.api_key = api_key
        self.version = version
        self.fetch_timeout = fetch_timeout

        self.url = '{}/{}'.format(self.SANDBOX_BASE_URL if is_sandbox else self.PRODUCTION_BASE_URL,
                                  version)
        self.session = self._init_session()

    def _init_session(self):
        session = requests.Session()
        session.headers.update({
            'Content-Type': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key,
        })

        return session

    def fetch(self, path, params=None):
        response = self.session.get(
            '{}{}'.format(self.url, path),
            params=params,
            timeout=self.fetch_timeout)

        return self.parse_response(response)

    @staticmethod
    def parse_response(response):
        response_dict = response.json()
        if response.status_code == 200:
            return response_dict['data']
        else:
            error_message = response_dict['status']['error_message']

            # https://pro.coinmarketcap.com/api/v1#section/Errors-and-Rate-Limits
            if response.status_code == 400:
                raise BadRequestException(error_message)
            elif response.status_code == 401:
                raise UnauthorizedException(error_message)
            elif response.status_code == 402:
                raise PaymentRequiredException(error_message)
            elif response.status_code == 403:
                raise ForbiddenException(error_message)
            elif response.status_code == 429:
                raise TooManyRequestsException(error_message)
            else:
                raise InternalServerErrorException(error_message)