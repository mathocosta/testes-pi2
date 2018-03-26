import fetch_politician_data as pd
from get_deputies_names import deputies

for d in deputies:
    p = pd.get_politician_data_by_name(d.name)
    if (p != None):
        print(p['name'])
    else:
        print("{0} não foi encontrado".format(d.name))
