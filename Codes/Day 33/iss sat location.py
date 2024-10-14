import requests

responce = requests.get(url="http://api.open-notify.org/iss-now.json")
responce.raise_for_status()

longitude = responce.json()["iss_position"]["longitude"]
latitude = responce.json()["iss_position"]["latitude"]

is_position = (latitude,longitude)
print(is_position)