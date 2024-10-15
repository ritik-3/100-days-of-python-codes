import requests

OWM_Endpint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "6a3f482683050c264a665c8a22ab3859"
MY_LAT = 23.259933
MY_LNG = 77.412613
parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LNG,
    "appid" : api_key,
    "cnt" : 4,
}


responce = requests.get(OWM_Endpint, params=parameters)
responce.raise_for_status()
weather_data = responce.json()
#print(weather_data["list"][0]["weather"][0])

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    
    if int(condition_code)<700:
        will_rain = True
        
if will_rain:
    print("its gonna rain... :)")