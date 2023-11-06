import requests
resource_uri = "http://www.omdbapi.com/"
params = {
"apikey": "56470f387c7d2f1a05a790af71d3e4fe",
"t": "Rocky"
}
response = requests.get(resource_uri, params)
response_data = response.json()
for key in response_data.keys():
    print(f"{key}: {response_data[key]}")



