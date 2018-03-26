import requests
from bs4 import BeautifulSoup
from politician import Politician

url = "www.al.ce.gov.br/paineldecontrole/folha/2018/anexo02.php?mes=fevereiro"
deputies = []

r = requests.get("http://" + url)
data = r.text

soup = BeautifulSoup(data, "html.parser")

for tr_tag in soup.find_all('tr'):
    children = tr_tag.find_all('font')

    if (len(children) == 3):
        d_name = ""
        d_number = ""
        d_status = ""

        if children[0] != None:
            d_name = children[0].string
        if children[1] != None:
            d_number = children[1].string
        if children[2] != None:
            d_status = children[2].string


        if (d_status == "PARLAMENTAR"):
            d = Politician(d_name, d_number, d_status)
            deputies.append(d)
