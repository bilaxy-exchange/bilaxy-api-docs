import hmac
import os
from datetime import datetime
from hashlib import sha256
from urllib.parse import urlencode

import requests

BILAXY_API_SERVER_URL = 'https://newapi.bilaxy.com'
BILAXY_API_KEY = os.getenv('BILAXY_API_KEY', '-PLEASE REPLACE ME-')
BILAXY_API_SECRET = os.getenv('BILAXY_API_SECRET', '-PLEASE REPLACE ME-')


def hmac_sha256(body: str, secret_key: str) -> str:
    return hmac.new(secret_key.encode(), body.encode(), digestmod=sha256).hexdigest()


def wrap_params(**params) -> str:
    basic_params = {'timestamp': int(datetime.now().timestamp() * 1000), 'apikey': BILAXY_API_KEY}
    params.update(basic_params)

    # 1. sorted params by keys
    params = sorted(params.items())
    # 2. urlencode params
    query = urlencode(params)
    # 3. make signature
    signature = hmac_sha256(query, BILAXY_API_SECRET)

    return f'{query}&signature={signature}'


def request_get(path, **params) -> requests.models.Response:
    query = wrap_params(**params)
    url = f'{BILAXY_API_SERVER_URL}{path}?{query}'
    r = requests.get(url)
    print(f'''
        url -> {url}
        status_code -> {r.status_code}
        result -> {r.content.decode()}
    ''')
    return r


def get_balances() -> requests.models.Response:
    return request_get('/v1/accounts/balances')


def get_order(order_id: int) -> requests.models.Response:
    return request_get('/v1/accounts/order', id=order_id)


def get_orders(pair: str, limit: int = None, sort: str = None, cursor: int = None, start: int = None, end: int = None) -> requests.models.Response:
    params = {'pair': pair}
    for k, v in [('limit', limit), ('sort', sort), ('cursor', cursor), ('start', start), ('end', end)]:
        if v is not None:
            params[k] = v
    return request_get('/v1/accounts/orders', **params)


def get_opened_orders(pair: str) -> requests.models.Response:
    return request_get('/v1/accounts/orders/opened', pair=pair)


def get_trades(pair: str, limit: int = None, sort: str = None, cursor: int = None, start: int = None, end: int = None) -> requests.models.Response:
    params = {'pair': pair}
    for k, v in [('limit', limit), ('sort', sort), ('cursor', cursor), ('start', start), ('end', end)]:
        if v is not None:
            params[k] = v
    return request_get('/v1/accounts/trades', **params)


def get_deposit_addresses(currency: str) -> requests.models.Response:
    return request_get('/v1/accounts/addresses/deposit', currency=currency)
