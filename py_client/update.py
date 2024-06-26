import requests


endpoint = "http://localhost:8000/api/products/6/update/"

data = {
    "title": "Wireles Mouse",
    "price": 37.99,
}

response = requests.put(endpoint, json=data)

print(response.json())
