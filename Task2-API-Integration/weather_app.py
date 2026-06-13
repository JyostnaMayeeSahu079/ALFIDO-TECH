import requests

def get_weather():

    city = input("Enter city name: ")

    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        current = data["current_condition"][0]

        print("\n===== WEATHER DETAILS =====")
        print("City:", city)
        print("Temperature:", current["temp_C"], "°C")
        print("Humidity:", current["humidity"], "%")
        print("Weather:", current["weatherDesc"][0]["value"])

    except requests.exceptions.ConnectionError:
        print("No Internet Connection!")

    except requests.exceptions.HTTPError:
        print("Invalid Request!")

    except Exception as e:
        print("Error:", e)

get_weather()