import requests
import json

# Creates an API call and stores the answer
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explores the data structure
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)