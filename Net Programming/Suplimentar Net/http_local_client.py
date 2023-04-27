import requests
r = requests.get("http://127.0.0.1:8080/", params={"name":'michael'})
print("Request method: GET, \
    Response status_code: {}, Response data: {}".format(r.status_code, r.text))
r = requests.post("http://127.0.0.1:8080/", params = {'name':'peter', 'last_name':'peterson'})
print("Request method: POST, \
    Response status_code: {}, Response data: {}".format(r.status_code, r.text))
r = requests.delete("http://127.0.0.1:8080/", params={'name':'Michael'})
print(f'Request method DELETE: Response status code: {r.status_code}, Response: {r.text}')