import requests
from pprint import pprint

# endpoint = "http://httpbin.org/status/200"
endpoint = "http://localhost:8000/api/products/1/"

response = requests.post(
    endpoint,
    json={"title": "ABC123", "content": "Hello World", "price": "123USD"},
)

pprint(response.headers)
pprint(response.json())
