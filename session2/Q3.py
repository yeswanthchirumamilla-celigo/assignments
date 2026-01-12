import requests


API_KEY = "4a10b673283554a0919213e6c8b5df53"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city_name):
    
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        return None
    except requests.exceptions.RequestException:
        print("Network error occurred.")
        return None


def display_weather(data):
    temperature = data["main"]["temp"]
    condition = data["weather"][0]["description"]

    print(f"\nTemperature: {temperature}°C")
    print(f"Condition: {condition.capitalize()}")


def main():
    city = input("Enter city name: ").strip()

    if not city:
        print("City name cannot be empty.")
        return

    weather_data = get_weather(city)

    if weather_data is None or weather_data.get("cod") != 200:
        print("City not found. Please enter a valid city name.")
    else:
        display_weather(weather_data)


if __name__ == "__main__":
    main()
