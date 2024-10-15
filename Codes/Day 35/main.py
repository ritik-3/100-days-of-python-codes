import requests

OWM_Endpint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "6a3f482683050c264a665c8a22ab3859"
MY_LAT = 23.259933
MY_LNG = 77.412613
parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LNG,
    "appid" : api_key
}


responce = requests.get(OWM_Endpint, params=parameters)

print(responce.json())