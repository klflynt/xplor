import requests

endpoint = "http://localhost:8000/fizzbuzz/"

data = {
    "message": "...looks like the Thalmor are with him."
}

get_response = requests.post(endpoint, json=data)

print(get_response.text)
# print(get_response.json())