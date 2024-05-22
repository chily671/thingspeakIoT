import requests
import json
CHANNEL_ID = ""
READ_API_KEY = ""
BASE_URL = "https://api.thingspeak.com"

def read_data(num_entries=20):
    url = f"{BASE_URL}/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results={num_entries}"

    try:
        response = requests.get(url)
        data = response.json()
        with open("data.json", "w") as json_file:
            json.dump(data, json_file)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error reading data: {e}")
        return None
    
data = read_data(10)  # Read the latest 10 entries
if data:
    for entry in data:
        print(entry) 