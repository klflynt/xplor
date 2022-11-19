import requests

endpoint = "http://localhost:8000/fizzbuzz/"


get_response = requests.get(endpoint)

print(get_response.text)
# print(get_response.json())