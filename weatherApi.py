import requests

api_key = "0b0ad04ec7874abd992104415240505"

user_input = input("Enter City/Country: ")

weather_data = requests.get(f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={user_input}")

weather = weather_data.json()["current"]["temp_c"]
name = weather_data.json()["location"]["name"]

print(f"Temp in Celcius is : {weather} for {name}")