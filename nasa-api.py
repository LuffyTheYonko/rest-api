# importing Required Libraries
import requests
import pandas as pd
import webbrowser

# storing generated api key
api_key = "jXdh3tAGtB3YyXp1m22ytL5oXbVofeFrsvOXnQIT"

# pulling data from api
api_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
response = requests.get(api_url)
data = response.json()
print(data)

# displaying image received from api

url = data['url']
webbrowser.open(url)

# setting parameters for api query

params = {
    "start_date": "2024-02-07"
}

# getting data from api

api_url = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={api_key}"
response = requests.get(api_url, params=params)
ast_data = response.json()

# extracting data from api

asteroid_data = []

for c in ast_data["near_earth_objects"]:
    for asteroid in ast_data["near_earth_objects"][c]:
        asteroid_id = asteroid["id"]
        asteroid_name = asteroid["name"]
        min_est_diameter = asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_min"]
        absolute_magnitude = asteroid["absolute_magnitude_h"]
        relative_velocity = asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"]
        asteroid_data.append([asteroid_id, asteroid_name, min_est_diameter, absolute_magnitude, relative_velocity])

# converting the data into a dataframe
columns = ["Asteroid ID", "Asteroid name", "The Minimal estimated diameter in Kilometre", "Absolute_magnitude",
           "Relative_velocity(km/s)"]

asteroid_df = pd.DataFrame(asteroid_data, columns=columns)
print(asteroid_df.head())

# exporting to a csv file

asteroid_df.to_csv("nasa_api data.csv")
