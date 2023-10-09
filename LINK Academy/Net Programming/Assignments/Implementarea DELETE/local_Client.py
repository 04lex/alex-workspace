import requests

r = requests.get('http://127.0.0.1:8000/', params={"name": "Alex"})
print(r.text)

r = requests.post('http://127.0.0.1:8000/', params={"name": "Mihai"})
print(r.text)

r = requests.delete('http://127.0.0.1:8000/', params={"name": "Daniel"})
print(r.text)