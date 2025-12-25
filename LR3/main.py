from my_open_weather import OpenWeatherClient

client = OpenWeatherClient(api_key="ab01cf693ca7bd5c16cf9c67a103cfb9")
print(client.current_weather("Saint Petersburg"))
data = client.current_weather("Saint Petersburg")

temp = data["main"]["temp"]
description = data["weather"][0]["description"]

print(f"Температура: {temp}°C")
print(f"Погода: {description}")
