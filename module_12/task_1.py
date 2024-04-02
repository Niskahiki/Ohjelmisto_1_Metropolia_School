import requests
from requests.exceptions import RequestException

try:
    response = requests.get("https://api.chucknorris.io/jokes/random")

    if response.status_code == 200:
        json_response = response.json()
        print(json_response['value'])
    else:
        print(f"Hakua ei pystytty suorittaa. status_code: {response.status_code}")


except RequestException as e:
    print(f"Hakua ei pystytty suorittaa. reason: {e}")