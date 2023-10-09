import requests
api_key ='7402487d'
url = f'http://www.omdbapi.com/?apikey=7402487d&t=Barbi'
print(url)
response = requests.get(url)
data = response.json()
print(data)
for key in data.keys():
    print(f'{key}={data[key]}')






