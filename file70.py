import requests

url = "https://jsonplaceholder.typicode.com/users"

res = requests.get(url).json()

for i in res:
    print(i['name'])