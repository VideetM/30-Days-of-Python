import requests

ngrok_url = "http://b7681ad8ef51.ngrok.io"
endpoint_url = f"{ngrok_url}/scraper"

r = requests.post(endpoint_url, json={})
print(r.json()['data'])