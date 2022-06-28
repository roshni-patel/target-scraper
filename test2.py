import json
import requests

url = "https://www.target.com/s?searchTerm=lego+duplo"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
}

api_url = "https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1"

params = {
    "key": "ff457966e64d5e877fdbad070f276d18ecec4a01",
    "channel": "WEB",
    "count": "24",
    "default_purchasability_filter": "false",
    "include_sponsored": "true",
    "keyword": "lego duplo",
    "offset": "0",
    "page": "/s/lego duplo",
    "platform": "desktop",
    "pricing_store_id": "3991",
    "useragent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "visitor_id": "AAA",
}

data = requests.get(api_url, params=params).json()

# uncomment this to print all data:
# print(json.dumps(data, indent=4))

for p in data["data"]["search"]["products"]:
    print(
        "{:<10} {}".format(
            p["price"]["current_retail"],
            p["item"]["product_description"]["title"],
        )
    )