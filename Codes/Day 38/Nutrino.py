import requests
from datetime import datetime

APP_ID = "bruh"
API_KEY = "need help XD"

# SHEETY_ENDPOINT = "https://api.sheety.co/0d1b815aa721de41e39ad277d16326ab/nutrinox/sheet1"
SHEETY_ENDPOINT = "https://api.sheety.co/0d1b815aa721de41e39ad277d16326ab/nutrinox/sheet1"
sheety_headers = {
    "Content-Type": "application/json"
}

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

user_input = input("Describe Your Exercise:-\n")

data = {
    "query": user_input,
    "gender": "male", 
    "weight_kg": 70,   
    "height_cm": 175,  
    "age": 25          
}

nutritionix_response = requests.post(url, json=data, headers=headers)
nutritionix_response.raise_for_status()

exercise_results = nutritionix_response.json()

current_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H:%M:%S")

for exercise in exercise_results["exercises"]:
    exercise_name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    
    workout_data = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise_name,
            "duration": duration,
            "calories": calories
        }
    }
    
    sheety_response = requests.post(SHEETY_ENDPOINT, json=workout_data, headers=sheety_headers)
    sheety_response.raise_for_status()
    print(f"Logged exercise: {exercise_name}, Duration: {duration} mins, Calories: {calories} kcal")

print("All exercises logged successfully.")