import requests
import json

data = {"name":"watermelon","quantity":3,"price":3.5,"type":"fruit"}

r = requests.post('http://127.0.0.1:5000/grocery/add', json=data)
print(r.json())