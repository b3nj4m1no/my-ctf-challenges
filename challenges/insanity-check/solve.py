import requests

url = "http://localhost:4567"

payload = '\ufeff{"givemeflag": true}'.encode('utf-8') 

r = requests.post(
    url,
    headers = {"Content-Type": "text/plain"},
    data = payload
)

print(r.text)