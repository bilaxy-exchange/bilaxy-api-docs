## 2020.12.12
- `/v1/orderbook` add the parameter `limit`, in order to limit the number of depths returned, the default is 30, and the maximum is 200.

## 2020.04.20

Added a portion of the documentation for the private API, optimizing the naming of some API URLs.
- Added the following private APIs.
    + `/v1/accounts/balances` 
    + `/v1/accounts/order` 
    + `/v1/accounts/orders` 
    + `/v1/accounts/orders/opened` 
    + `/v1/accounts/trades` 
    + `/v1/accounts/addresses/deposit` 

- Updated url `/v1/valuation-calculator` to `/v1/valuation`.
- Updated url `/v1/rate_limits` to `/v1/ratelimits`.
- Updated the `/v1/ratelimits` result format.
    + Before the update
        ```
        [
          {	
            "interval": "10s",
            "max_times": 100
          }
        ]
        ```
    + After the update
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
