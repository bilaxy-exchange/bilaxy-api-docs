import hmac
import os
import typing
import json
from datetime import datetime
from decimal import Decimal
from hashlib import sha256
from urllib.parse import urlencode

import requests

BILAXY_API_SERVER_URL = 'https://newapi.bilaxy.com'
BILAXY_API_KEY = os.getenv('BILAXY_API_KEY', '-PLEASE REPLACE ME-')
BILAXY_API_SECRET = os.getenv('BILAXY_API_SECRET', '-PLEASE REPLACE ME-')


def hmac_sha256(body: str, secret_key: str) -> str:
    return hmac.new(secret_key.encode(), body.encode(), digestmod=sha256).hexdigest()


def make_signature(params: typing.Dict = None) -> typing.Tuple[str, str]:
    # 1. sorted params by keys
    params = sorted(params.items())
    # 2. urlencode params
    query = urlencode(params)
    # 3. make signature
    return query, hmac_sha256(query, BILAXY_API_SECRET)


def wrap_params(**params) -> str:
    basic_params = {'timestamp': int(datetime.now().timestamp() * 1000), 'apikey': BILAXY_API_KEY}
    params.update(basic_params)

    query, signature = make_signature(params)
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


def wrap_body(data):
    body = {}
    basic_params = {'timestamp': int(datetime.now().timestamp() * 1000), 'apikey': BILAXY_API_KEY}
    body.update(basic_params)
    body.update(data)
    _, signature = make_signature(body)
    basic_params.update({'signature': signature})
    query = urlencode(basic_params)

    return query


def request_for_body(method, path, data) -> requests.Response:
    query = wrap_body(data)
    url = f'{BILAXY_API_SERVER_URL}{path}?{query}'
    r = requests.request(method, url, json=data)
    print(f'''
        url -> {url}
        data -> {json.dumps(data)}
        status_code -> {r.status_code}
        resp_headers -> {r.headers}
        result -> {r.content.decode()}
    ''')
    return r


def get_balances() -> requests.Response:
    return request_get('/v1/accounts/balances')


def get_order(order_id: int, pair: str) -> requests.Response:
    return request_get('/v1/accounts/order', id=order_id, pair=pair)


def get_orders(pair: str, limit: int = None, sort: str = None, cursor: int = None, start: int = None, end: int = None) -> requests.Response:
    params = {'pair': pair}
    for k, v in [('limit', limit), ('sort', sort), ('cursor', cursor), ('start', start), ('end', end)]:
        if v is not None:
            params[k] = v
    return request_get('/v1/accounts/orders', **params)


def get_opened_orders(pair: str) -> requests.Response:
    return request_get('/v1/accounts/orders/opened', pair=pair)


def get_trades(pair: str, limit: int = None, sort: str = None, cursor: int = None, start: int = None, end: int = None) -> requests.Response:
    params = {'pair': pair}
    for k, v in [('limit', limit), ('sort', sort), ('cursor', cursor), ('start', start), ('end', end)]:
        if v is not None:
            params[k] = v
    return request_get('/v1/accounts/trades', **params)


def get_deposit_addresses(currency: str) -> requests.Response:
    return request_get('/v1/accounts/addresses/deposit', currency=currency)


def create_order(pair: str, price: Decimal, quantity: Decimal, side: str) -> requests.Response:
    data = {'pair': pair, 'price': str(price), 'quantity': str(quantity), 'side': side}
    r = request_for_body('POST', '/v1/accounts/orders', data)
    return r


def cancel_order(pair: str, order_id: str) -> requests.Response:
    data = {'pair': pair, 'id': order_id}
    r = request_for_body('DELETE', '/v1/accounts/orders', data)
    return r


if __name__ == '__main__':
    r = create_order('BTC_USDT', Decimal('20000'), Decimal('0.001'), 'sell')
    id_str = r.json().get('id')
    if id_str:
        cancel_order('BTC_USDT', id_str)
