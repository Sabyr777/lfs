import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'future_step':2005})

print(r.json())