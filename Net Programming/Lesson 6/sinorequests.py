import requests

url = 'https://api.datamuse.com/words'

params_rime = {'rel_rhy':'pretty'}
params_sinonime = {'ml':'women'}

resp = requests.get(url, params_sinonime)

resp.content # -> raspunsul json

# iau modul json
import json

# transform continutul intr-o lista
continut = json.loads(resp.content)

# iterez prin lista, luand fiecare dictionar, cu cheia 'word', fac o noua lista
cuvinte = [ i['word'] for i in continut]

print(cuvinte)