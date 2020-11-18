import requests
import json
import time

access_token = "14b1c73e-c37e-3f0c-8aac-969b58de6e14"


def jprint(obj):
    """ serialization of json """
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# 88359856700013
def api_insee(siret):
    """ get  request from INSEE API """
    url4 = f"https://api.insee.fr/entreprises/sirene/V3/siret/{siret}"
    result = requests.get(
        url4,
        headers={'Content-Type': 'application/json',
                 'Authorization': 'Bearer {}'.format(access_token)})

    """ retrieving the APE code """
    print(result.status_code)
    #jprint(result.json())
    if result.status_code == 200:
        time.sleep(1)
        """ de-serialization of json """
        # jprint(result.json())
        json_data = json.loads(result.text)
        # print("Le code APE est:")
        print(json_data['etablissement']['periodesEtablissement'][0]['activitePrincipaleEtablissement'], "INSEE ***")
    else:
        print("bad request")


# print(response.status_code)
# jprint(result.json())
# if response.status_code == 200:
# info.append(response)

# for key, value in response.items():
#     print('Num RCS -------------->  ', value["activite_principale"])
#     print('Categorie juridique -->  ', value["categorie_juridique"])
