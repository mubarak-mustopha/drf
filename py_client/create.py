import requests

endpoint = "http://localhost:8000/api/products/"

response = requests.post(endpoint, json={"title": "A5_Pro Pouch", "price": 4.99})

print(response.json())
