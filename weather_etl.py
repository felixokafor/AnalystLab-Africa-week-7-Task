# import requests
# API_KEY = "b7f11758beec8af2acf5054bbc4c13c7"
# City = "Lokoja"
# url = f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_KEY}&units=metric"

# response = requests.get(url)
# data = response.json()

# print(response.status_code)
# print(response.json())


# Extracting only data fields that i need 
import requests
import pandas as pd
from datetime import datetime 

API_KEY = "b7f11758beec8af2acf5054bbc4c13c7"
cities = ["Lokoja", "Abuja", "Lagos", "Port Harcourt", "Ilorin", "Anambra"]

weather_data = []

for city in cities:
    print(f"Getting data for {city}...")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    print("Status Code:", response.status_code)
    data = response.json()
    print(data)
# Extracting only data fields that i need
    weather_data.append({
        "City": city,
        "Temperature": data["main"]["temp"],
        "Humidity": data["main"]["humidity"],
        "Weather Condition": data["weather"][0]
["main"],
        "Wind Speed": data["wind"]["speed"],
        "Date Time": datetime.now()
    })

df = pd.DataFrame(weather_data)

df.rename(columns={
    "Date Time": "Timestamp"
}, inplace=True)


print("\nDataset info")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

print("\nData Types")
print(df.dtypes)

# csv file export
df.to_csv("process_weather_data.csv",
index=False)

# city with highest temperature
highest_temp_city = df.loc[df["Temperature"].idxmax()]

print("\ncity with Highest Temperature:")
print(highest_temp_city["City"])
print("Temperature:", highest_temp_city["Temperature"], "°C")

# City with highest humidity
highest_humidity_city = df.loc[df["Humidity"].idxmax()]

print("\ncity with Highest Humidity:")
print(highest_humidity_city["City"])
print("Humidity:", highest_humidity_city["Humidity"], "%")

# Average temperature
average_temp = df["Temperature"].mean()

print("\nAverage Temperature Across cities:")
print(round(average_temp, 2), "°C")

# Weather Condition count
print("\nWeather Conditions:")
print(df["Weather Condition"].value_counts())

print("\nDataset saved successfully!")

print("\nFinal DataFrame:")
print(df)