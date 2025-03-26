import requests

# URL for the dataset
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# Fetch the dataset
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the dataset to a file
    with open("cso.json", "w") as file:
        file.write(response.text)
    print("Dataset saved as cso.json")
else:
    print(f"Failed to fetch dataset. HTTP Status Code: {response.status_code}")