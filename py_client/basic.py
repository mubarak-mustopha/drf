import requests
from pprint import pprint

# endpoint = "http://httpbin.org/status/200"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(
    endpoint,
    params={"abc": 123},
    json={"query": "Django"},
)
pprint(get_response.text)
print(get_response.status_code)
