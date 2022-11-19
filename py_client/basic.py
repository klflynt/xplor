import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"message": "Hello there"})

print(get_response.text)
print(get_response.json())