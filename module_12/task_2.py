import requests
from requests.exceptions import RequestException


def get_city_location(city_name: str) -> tuple | str:

    try:
        result = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid"
                              f"=fd8ddf164069d8485b8e7b0a16079b21")

        if result.status_code == 200:
            json_result = result.json()
            location = (json_result[0]['lat'], json_result[0]['lon'])

            return location

        else:
            return f"Result status code was not 200. Result status code was: {result.status_code}"

    except RequestException as e:
        return f"Error occurred while getting city location. Error: {e}"


def get_weather(location: tuple) -> tuple or str:

    try:
        result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={location[0]}&lon={location[1]}" 
                              f"&units=metric&appid=fd8ddf164069d8485b8e7b0a16079b21")

        if result.status_code == 200:
            json_result = result.json()
            weather = (json_result['weather'][0]['main'], json_result['main']['temp'])

            return weather
        else:
            return f"Result status code was not 200. Result status code was: {result.status_code}"

    except RequestException as e:
        return f"Error occurred while getting city weather. Error {e}"


def main():
    usr_city = input("Anna kaupunki: ")

    city_location = get_city_location(usr_city)

    if type(city_location) is str:
        print(city_location) ## If any issues/problems have occurred in get_city_location() then the reason is printed to usr

    else:
        weather = get_weather(city_location)

        if type(weather) is str:
            print(weather)

        else:
            print(f"Sää: {weather[0]}. Lämpötila: {weather[1]}°C")


if __name__ == "__main__":
    main()
