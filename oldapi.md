# General Old API Information
- The old API base endpoint is: https://api.bilaxy.com


### Auth
Each time you request the private API, you need to validate the signature, and the POST parameter sample:
`param = ['amount=1', 'price=10000', 'type=buy', 'key=***', 'sign=***'].join('&')`
The 'sign' is a signature, you can get sign by first sort parameters(amount、price、type、key、secret) with ascending order, then join with '&' and finally encrpted with sha1. You don't need to post secret as parameter.

### /v1/cancel_trade
Cancel order.
API-key requires `ALL` permissions.

**Method:** `POST`

**Parameters:**
Name | Type | Required | Description
------------|------------|------------|------------
id | long | true | order id.
symbol | int | true | Symbol id.
key | string | true | API key.
sign | string | true | signature.

**Response:**
```
{
    "code": 200, 
    "data": "11111"
}
```

### /v1/trade
Create order.
API-key requires `ALL` permissions.

**Method:** `POST`

**Parameters:**
Name | Type | Required | Description
------------|------------|------------|------------
symbol | int | true | Symbol id.
amount | string | true | amount.
price | string | true | price.
type | string | true | `buy` or `sell`.
key | string | true | API key.
sign | string | true | signature.

**Response:**
```
{
    "code": 200, 
    "data": "11111"
}
```

## Python demo (create order)
```
import hashlib
import requests
import os

# The following process shows how to create the signature that must be verified through the bilaxy API
param = "&".join(sorted([
    'symbol=119',
    'amount=27.04392634',
    'price=0.00006109',
    'type=buy',
    'key='+os.getenv("API_KEY"),
    'secret='+os.getenv("API_SECRET")

]))

# Create signature from above Parameters
signature = hashlib.sha1(param.encode('UTF-8')).hexdigest()


# place a limit trade
api_endpoint = "https://api.bilaxy.com/v1/trade"

# load relevant parameters
PARAMS = {'symbol':'119',
          'amount':'27.04392634',
          'price':'0.00006109',
          'type':'buy',
          'key':os.getenv("API_KEY"),
          'sign':signature}

# execute trade and save to r object
# This instruction requires a "POST" method while others require a "GET" Take Note
r = requests.post(url = api_endpoint, data = PARAMS)

# Check if trade was placed
if r.json()['resultCode'] == 0:
    print("Trade was placed!")
```
