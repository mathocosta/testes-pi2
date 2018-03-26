import requests
import json
from politician import Politician

r = requests.get("http://politicos.olhoneles.org:80/api/v0/politicians/?limit=50&candidacies__elected=true&candidacies__state__slug=ceara&candidacies__political_office__slug=deputado-estadual&candidacies__election_round__election__year=2014&state__siglum=CE")
json_data = r.json()

# {
#   "meta": {
#     "previous": "",
#     "total_count": "int",
#     "offset": "int",
#     "limit": "int",
#     "next": ""
#   },
#   "objects": {
#     "politicians": [
#       {
#         "website": "",
#         "picture": "",
#         "about": "",
#         "alternative_names": "related",
#         "name": "",
#         "political_parties": "related",
#         "gender": "",
#         "marital_status": "related",
#         "cpf": "",
#         "email": "",
#         "candidacies": "related",
#         "state": "related",
#         "date_of_birth": "date",
#         "resource_uri": "",
#         "place_of_birth": "",
#         "id": 0,
#         "nationality": "related",
#         "education": "related",
#         "events": "related",
#         "ethnicity": "related",
#         "occupation": "related"
#       }
#     ]
#   }
# }
def get_politician_data_by_name(name):
    for c in json_data['objects']:
        if (c['name'].upper() == name):
            return c

    return None
