import requests

# autentificare si get token
def login(numar_cont, parola):
    data = {'numar_cont': numar_cont, 'parola': parola}
    response = requests.post('http://127.0.0.1:5000/login', json=data)
    if response.status_code == 200:
        return response.json()['token']
    else:
        return None
    

# afisare date prin token
def get_cont_details(token):
    headers = {'Authorization': token}
    response = requests.get('http://127.0.0.1:5000/cont', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
# ex user 1
if __name__ == '__main__':
    numar_cont = 'user1'
    parola = 'parola123'

    token = login(numar_cont, parola)
    if token:
        cont_details = get_cont_details(token)
        if cont_details:
            print('Detalii cont:', cont_details)
        else:
            print('Datele contului nu au putut fi obtinute')
    else:
        print('Eroare de autentificare')