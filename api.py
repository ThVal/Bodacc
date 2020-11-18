import requests
import json

from api_insee import api_insee


def jprint(obj):
    """ create a formatted string of the Python JSON object """
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def api_request(siren):
    # time.sleep(2)
    url3 = f"https://entreprise.data.gouv.fr/api/sirene/v3/unites_legales/{siren}"
    response = requests.get(url3)
    if response.status_code == 200:
        json_data = json.loads(response.text)
        try:
            # print(json_data['unite_legale']['siren'])
            x = json_data['unite_legale']['etablissements'][0]['siret']
            # jprint(response.json())
            # print(x)
            print(json_data['unite_legale']['etablissement_siege']['activite_principale'])
        except:
            api_insee(json_data['unite_legale']['etablissements'][0]['siret'])
