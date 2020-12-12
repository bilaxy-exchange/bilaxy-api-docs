<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [General API Information](#general-api-information)
- [Http Status Codes](#http-status-codes)
- [Error Codes](#error-codes)
- [Public API Endpoints](#public-api-endpoints)
  - [General endpoints](#general-endpoints)
    - [/health](#health)
    - [/ratelimits](#ratelimits)
  - [Market Info endpoints](#market-info-endpoints)
    - [/v1/pairs](#v1pairs)
    - [/v1/currencies](#v1currencies)
    - [/v1/orderbook](#v1orderbook)
    - [/v1/trades](#v1trades)
    - [/v1/ticker/24hr](#v1ticker24hr)
    - [/v1/valuation](#v1valuation)
- [Private API Endpoints](#private-api-endpoints)
  - [About signature](#about-signature)
  - [About timestamp](#about-timestamp)
  - [Account endpoints](#account-endpoints)
    - [/v1/accounts/balances](#v1accountsbalances)
    - [/v1/accounts/order](#v1accountsorder)
    - [/v1/accounts/orders](#v1accountsorders)
    - [/v1/accounts/orders/opened](#v1accountsordersopened)
    - [/v1/accounts/trades](#v1accountstrades)
    - [/v1/accounts/addresses/deposit](#v1accountsaddressesdeposit)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# General API Information
- The base endpoint is: https://newapi.bilaxy.com

# Http Status Codes
- Please refer to https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# Error Codes
Any endpoint can return an ERROR
- 1001 - Not found API-key or API-key format invalid.
- 1002 - Invalid API-key or permissions for action.
- 1003 - Signature for this request is not valid.
- 1004 - Timestamp cannot be 1000ms later than server time, no earlier than server time 5000ms.
- 1005 - Currency's deposit is disabled.


Example:
```
{
    "code": 400,
    "msg": "`pair` is required.",
    "detail": null
}
```

# Public API Endpoints

## General endpoints

### /health
Test connection to RestAPI and get server time.

**Method:** `GET`

**Parameters:** `None`

**Response:**
```
{
  "human_time": "2019-12-03T03:08:56.553",
  "timestamp": 1575342536553,
  "timezone": "UTC"
}
```

### /ratelimits
Returns the rate limit for all api calls for a single ip.

**Method:** `GET`

**Parameters:** `None`

**Response:**
```
[
  {
    "group": "default",
    "path": "all",
    "by": "ip",
    "period": "1s",
    "max_times": 10
  },
  {
    "group": "public",
    "path": "all",
    "by": "ip",
    "period": "1s",
    "max_times": 10
  },
  {
    "group": "private",
    "path": "all",
    "by": "ip",
    "period": "1s",
    "max_times": 10
  }
]
```

**Tips:**

All endpoints response headers contain the following information:

Name | Type | Description
------------|------------|------------
x-ratelimit-limit | integer | Total allowed calls.
x-ratelimit-remaining | integer | Remaining calls.
x-ratelimit-reset | integer | Timestamp when calls were restored.

## Market Info endpoints

### /v1/pairs
Returns trading pairs.

**Method:** `GET`

**Parameters:**

Name | Type | Required | Description
------------|------------|------------|------------
pair | string | false | Specify the name of the trading pair, such as `BTC_USDT`.

**Response:**
```
{
  "BTC_USDT": {
    "pair_id": 113,
    "base": "BTC",
    "quote": "USDT",
    "price_precision": 2,
    "amount_precision": 6,
    "min_amount": "0.0015",
    "max_amount": "+∞",
    "min_total": "10.0",
    "max_total": "+∞",
    "trade_enabled": true,
    "closed": false
  }
}
```

### /v1/currencies
Returns currencies information.

**Method:** `GET`

**Parameters:**

Name | Type | Required | Description
------------|------------|------------|------------
currency | string | false | Specify the name of the currency name, such as `BTC`.

**Response:**
```
{
  "BTC": {
    "currency": "BTC",
    "fullname": "Bitcoin",
    "min_withdraw": "0.002",
    "max_withdraw": "10.0",
    "fixed_withdraw_fee": "0,0007",
    "percent_withdraw_fee": "0.0",
    "withdraw_fee_currency_name": "BTC",
    "withdraw_enabled": true,
    "deposit_enabled": true
  }
}
```

### /v1/orderbook
Returns the depth data of a single trading market.

**Method:** `GET`

**Parameters:**

Name | Type | Required | Description
------------|------------|------------|------------
pair | string | true | Specify the name of the trading pair, such as `BTC_USDT`.
limit | integer | false | The number of depths returned, the maximum is 200, the default is 30.

**Response:**
```
{
  "timestamp": 1575354531459,
  "bids": [
    [
      "7288.04",
      "1.926909"
    ],
    [
      "7287.73",
      "0.492821"
    ]
  ],
  "asks": [
    [
      "7290.21",
      "0.170287"
    ],
    [
      "7290.22",
      "0.017168"
    ]
  ]
}
```


###  /v1/trades
Returns recent trading history for a single market.

**Method:** `GET`

**Parameters:**

Name | Type | Required | Description
------------|------------|------------|------------
pair | string | true | Specify the name of the trading pair, such as `BTC_USDT`
limit | integer | false | Number of trades history. Default 100, max 2000.

**Response:**
```
[
  {
    "id": 734733434,
    "price": "7175.70",
    "amount": "0.189702",
    "total": "1361.24464140",
    "ts": 1587369062716,
    "direction": "sell"
  },
  {
    "id": 734733433,
    "price": "7175.84",
    "amount": "0.413760",
    "total": "2969.07555840",
    "ts": 1587369062708,
    "direction": "sell"
  }
]
```


### /v1/ticker/24hr
Get ticker data for trading pairs.

**Method:** `GET`

**Parameters:**

Name | Type | Required | Description
------------|------------|------------|------------
pair | string | false | Specify the name of the trading pair, such as `BTC_USDT`.

**Response:**
```
{
  "BTC_USDT": {
    "height": "7398.34",
    "open": "7205.63",
    "low": "7183.7",
    "close": "7299.62",
    "base_volume": "60716.093839",
    "quote_volume": "443353854.13279493",
    "price_change": "0.013044",
    "trade_enabled": true
  }
}
```


### /v1/valuation
Get currency's BTC, USD and CNY valuation.

**Method:** `GET`

**Parameters:**

Name | Type | Required | Description
------------|------------|------------|------------
currency | string | false | Specify the name of the currency, such as `ETH`.

**Response:**
```
{
  "ETH": {
    "btc_value": "0.0230850000",
    "usd_value": "157.2425541000",
    "cny_value": "1084.8163807359"
  }
}
```

# Private API Endpoints

## About signature
- `private` endpoints require an additional parameter `signature`, to be sent in the query string or request body.
- `private` endpoints use `HMAC SHA256` signatures. The `HMAC SHA256 signature` is a keyed `HMAC SHA256` operation. Use your `secretKey` as the key and `all params` as the value for the HMAC operation.

## About timestamp
- A `private` endpoint also requires a parameter `timestamp`, to be sent which should be the millisecond timestamp of when the request was created and sent.
- `timestamp` cannot be 1000ms later than server time, no earlier than server time 5000ms.

## Account endpoints

### /v1/accounts/balances
Get user balances.
API-key requires `READONLY` or `ALL` permissions.

**Method:** `GET`

**Parameters:**
Name | Type | Required | Description
------------|------------|------------|------------
timestamp | timestamp(ms) | true | Current request timestamp(ms).
apikey | string | true | .
signature | string | true | .

**Response:**
```
{
  "BTC": {
    "available": 0.3851212,
    "used": 0
  },
  "ETH": {
    "available": 0.12,
    "used": 0.346
  },
  "USDT": {
    "available": 39.289,
    "used": 0
  }
}
```

### /v1/accounts/order
Get order by id.
API-key requires `READONLY` or `ALL` permissions.

**Method:** `GET`

**Parameters:**
Name | Type | Required | Description
------------|------------|------------|------------
id | long | true | Order id.
timestamp | timestamp(ms) | true | Current request timestamp(ms).
apikey | string | true | .
signature | string | true | .

**Response:**
```
{
    "id": 4141252868,
    "user_id": 1024,
    "price": 7012.5,
    "amount": 0.008939,
    "total": 62.6847375,
    "filled_total": 0,
    "created_at": "2020-04-06T13:56:55Z",
    "pair_name": "BTC_USDT",
    "direction": "sell",
    "filled_amount": 0,
    "state": "canceled"
}
```

### /v1/accounts/orders
Get user orders.
API-key requires `READONLY` or `ALL` permissions.

**Method:** `GET`

**Parameters:**
Name | Type | Required | Description
------------|------------|------------|------------
pair | string | true | Pair name. such as `BTC_USDT`.
limit | integer | false | `1~1000`, default `100`.
sort | string | false | `ASC` or `DESC`, default `DESC`.
cursor | long | false | `Order id`. If `sort` is `ASC`, filter out orders less than cursor, if `DESC`, filter out orders larger than cursor.
start | timestamp(ms) | false | Start time. Orders can only be queried for up to 90 days.
end | timestamp(ms) | false | End time. Orders can only be queried for up to 90 days.
timestamp | timestamp(ms) | true | Current request timestamp(ms).
apikey | string | true | .
signature | string | true | .

**Response:**
```
[
  {
    "id": 4141252868,
    "price": 7012.5,
    "amount": 0.008939,
    "total": 62.6847375,
    "filled_total": 0,
    "created_at": "2020-04-06T13:56:55Z",
    "pair_name": "BTC_USDT",
    "direction": "sell",
    "filled_amount": 0,
    "state": "canceled"
  },
  {
    "id": 4141252867,
    "price": 6958.74,
    "amount": 0.884606,
    "total": 6155.74315644,
    "filled_total": 0,
    "created_at": "2020-04-06T13:56:54Z",
    "pair_name": "BTC_USDT",
    "direction": "buy",
    "filled_amount": 0,
    "state": "non-filled"
  }
]
```

### /v1/accounts/orders/opened
Get user all opened orders.
API-key requires `READONLY` or `ALL` permissions.

**Method:** `GET`

**Parameters:**
Name | Type | Required | Description
------------|------------|------------|------------
pair | string | true | Pair name. such as `BTC_USDT`.
timestamp | timestamp(ms) | true | Current request timestamp(ms).
apikey | string | true | .
signature | string | true | .

**Response:**
```
[
  {
    "id": 4141252871,
    "price": 6998,
    "amount": 0.71327,
    "total": 4991.46346,
    "filled_total": 0,
    "created_at": "2020-04-06T13:57:03Z",
    "pair_name": "BTC_USDT",
    "direction": "sell",
    "filled_amount": 0,
    "state": "non-filled"
  },
  {
    "id": 4141252870,
    "price": 6999.9,
    "amount": 0.008887,
    "total": 62.2081113,
    "filled_total": 0,
    "created_at": "2020-04-06T13:57:01Z",
    "pair_name": "BTC_USDT",
    "direction": "sell",
    "filled_amount": 0,
    "state": "non-filled"
  }
]
```

### /v1/accounts/trades
Get user all trades.
API-key requires `READONLY` or `ALL` permissions.

**Method:** `GET`

**Parameters:**
Name | Type | Required | Description
------------|------------|------------|------------
pair | string | true | Pair name. such as `BTC_USDT`.
limit | integer | false | `1~1000`, default `100`.
sort | string | false | `ASC` or `DESC`, default `DESC`.
cursor | long | false | `Trade id`. If `sort` is `ASC`, filter out trades less than cursor, if `DESC`, filter out trades larger than cursor.
start | timestamp(ms) | false | Start time. Trades can only be queried for up to 90 days.
end | timestamp(ms) | false | End time. Trades can only be queried for up to 90 days.
timestamp | timestamp(ms) | true | Current request timestamp(ms).
apikey | string | true | .
signature | string | true | .

**Response:**
```
[
  {
    "id": 716797287,
    "order_id": 4141266876,
    "total": 0.0345,
    "price": 0.0000345,
    "amount": 1000,
    "created_at": "2020-04-10T19:00:14Z",
    "role": "taker",
    "direction": "buy",
    "pair": "BIA_ETH",
    "fees": 0.96189591,
    "fees_currency": "BIA"
  },
  {
    "id": 716797286,
    "order_id": 4141266829,
    "total": 0.0345,
    "price": 0.0000345,
    "amount": 1000,
    "created_at": "2020-04-10T18:59:11Z",
    "role": "maker",
    "direction": "sell",
    "pair": "BIA_ETH",
    "fees": 0.96189591,
    "fees_currency": "BIA"
  }
]
```

### /v1/accounts/addresses/deposit
Get user deposit addresses.
API-key requires `READONLY` or `ALL` permissions.

**Method:** `GET`

**Parameters:**
Name | Type | Required | Description
------------|------------|------------|------------
currency | string | true | Currency name. such as `BTC`.
timestamp | timestamp(ms) | true | Current request timestamp(ms).
apikey | string | true | .
signature | string | true | .

**Response:**
```
[
  "3Fbg7sVAYopLP6PhEtTJYzDojc9NNPr4vW"
]
```
