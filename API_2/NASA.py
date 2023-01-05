import requests, os

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

api_key = "o0U1fyym9QjCEarPABPI1Nuy40n5mGn0jmpmXxV2"
query_params = {"api_key": api_key, "earth_date": "2020-07-01"}

response = requests.get(endpoint, params=query_params)

response.json()
photos = response.json()["photos"]
print(f"Found {len(photos)} photos")

photos[4]["img_src"]