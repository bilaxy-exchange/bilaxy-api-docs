<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [General API Information](#general-api-information)
- [Http Return Codes](#http-return-codes)
- [Error Codes](#error-codes)
- [Public API Endpoints](#public-api-endpoints)
  - [General endpoints](#general-endpoints)
    - [/health](#health)
    - [/rate_limits](#rate_limits)
  - [Market Info endpoints](#market-info-endpoints)
    - [/v1/pairs](#v1pairs)
    - [/v1/currencies](#v1currencies)
    - [/v1/orderbook](#v1orderbook)
    - [/v1/trades](#v1trades)
    - [/v1/ticker/24hr](#v1ticker24hr)
    - [/v1/valuation-calculator](#v1valuation-calculator)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# General API Information
- The base endpoint is: https://newapi.bilaxy.com

# Http Return Codes
- Please refer to https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# Error Codes
- Any endpoint can return an ERROR

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

### /rate_limits
Returns the rate limit for all api calls for a single ip.

**Method:** `GET`

**Parameters:** `None`

**Response:**
```
[
  {
    "interval": "10s",
    "max_times": 100
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
    "withdraw_fee_currency_id": 2,
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


### /v1/valuation-calculator
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




