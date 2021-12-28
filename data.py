import requests

URL = 'https://opentdb.com/api.php'

PARAMS = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}

request = requests.get(URL, PARAMS)

question_data = request.json()["results"]

