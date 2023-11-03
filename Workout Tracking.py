import requests
from datetime import datetime

GENDER = "MALE"
WEIGHT_KG = 63
HEIGHT_CM = 128.00
AGE = 18

APP_ID = "6db8970a"

API_KEY = "ae305ff1a0d1b7eb72aa07c6f77dcf62"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint =  "VkFJUkFWRVNIV0FSQU46VkFJUkFWRVNIMTIz"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("10/3/23")
now_time = datetime.now().strftime("10")

for exercise in result["name"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["workout"].title(),
            "duration": exercise["duration_minute"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)