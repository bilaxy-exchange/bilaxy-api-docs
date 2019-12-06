# Websocket Stream for Bilaxy

#### wss://bilaxy.com/stream
Returns three types of data: depth, ticker, and trade.

**Parameters:**

Name | Type | Required | Description
--------|--------|--------|--------
symbol | integer | true | Specify trade pair ID.

**Response:**

Name | Type | Description
--------|--------|--------
symbol | integer | Specify trade pair ID.
method | string | `depth` or `ticker` or `trade`.
result | object | The result types of different methods are different, see below for details.

- depth data

Name | Type | Description
--------|--------|--------
ts | integer | timestamp.
b | array | Buy order depth data.The first item is `price`, the second item is `amount`, and the third item is `total`. Sort by descending price.
a | array | Sell order depth data.The first item is `price`, the second item is `amount`, and the third item is `total`. Sort by ascending price.
```
{
  "symbol": "113",
  "method": "depth",
  "result": {
    "ts": 1575612035641,
    "b": [
      [
        7391.3,
        1.921714,
        14203.9646882
      ],
      [
        7391.29,
        0.435503,
        3218.9289688699996
      ]
    ],
    "a": [
      [
        7393.7,
        0.021128,
        156.2140936
      ],
      [
        7393.76,
        0.52667,
        3894.0715792
      ]
    ]
  }
}
```
- 24 hour ticker data

Name | Type | Description
--------|--------|--------
ts | integer | timestamp.
c | decimal | Closing price.
h | decimal | Highest price.
l | decimal | Lowest price.
v | decimal | Quote trade volume.
rf | decimal | Price rise and fall. 
```
{
  "symbol": "113",
  "method": "ticker",
  "result": {
    "ts": 1575612419775,
    "c": 7383.43,
    "h": 7483.39,
    "l": 7263.4,
    "v": 59360.895796,
    "rf": 0.012122
  }
}
```
- Orders traded data

Name | Type | Description
--------|--------|--------
ts | integer | timestamp.
id | integer | Order id.
p | decimal | Price.
q | decimal | Amount(Quote Volume).
buy | boolean | Is buy or sell.
```
{
  "symbol": "113",
  "method": "trade",
  "result": [
    {
      "ts": 1575613541609,
      "id": 266369580,
      "p": 7372.07,
      "q": 0.102602,
      "buy": true
    },
    {
      "ts": 1575613541598,
      "id": 266369578,
      "p": 7372.02,
      "q": 0.27376,
      "buy": true
    }
  ]
}
```
