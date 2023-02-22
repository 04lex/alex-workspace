import requests
import json
import pprint

url = 'https://api.nationalize.io/?name=alexandru'

raspuns = requests.get(url)
continut = raspuns.content

print(continut)

deserizalizare = json.loads(continut)
# pprint(deserizalizare)
# print(type(deserizalizare))
pprint((deserizalizare['country']))

probabilitati = [ i['probability'] for i in deserizalizare['country'] ]
print(probabilitati)

media_prob = sum(probabilitati) / len(probabilitati)
print(media_prob)

deviatii = [abs(i - media_prob) for i in probabilitati]
print(deviatii)

deviatia_minima = min(deviatii)
print(deviatia_minima)

index = deviatii.index(deviatia_minima)
print(index)
print(deserizalizare['country'][index]['country_id'])
