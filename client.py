import requests

choice = int(input("1 ou 2 : "))
amount = int(input("nombre : "))

url = (f"http://localhost:8000?choice={choice}&amount={amount}")
payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)   
