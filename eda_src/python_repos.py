import requests

# Creates an API call and verifies the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept":"application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Converts the response object into a dictionary
response_dict = r.json()

# Processes the results
print(response_dict.keys())