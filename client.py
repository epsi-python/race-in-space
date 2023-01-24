import requests

url = "http://localhost:8000?choice=1&amount=190"

choice = input(type=int)
amount = input(type=int)

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
