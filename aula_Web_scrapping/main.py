from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.gov.br/receitafederal/pt-br/assuntos/agenda-tributaria/agenda-tributaria-2020/agenda-tributaria-janeiro-2020/dia-06-01-2020'
html = urlopen(url)

bs = BeautifulSoup(html, 'html.parser')

linhas = bs.find_all('tr', {'class': 'even'})

# Imprime todo texto contido nas linhas
for linha in linhas:
    print(linha.text)

codigo, descricao, periodo = [], [], []

# Adicionar valores nas listas
for linha in linhas:
    children = linha.findChildren('td')
    codigo.append(children[0].text)
    descricao.append(children[1].text)
    periodo.append(children[2].text)

df = pd.DataFrame({'Codigo': codigo, 'Descricao': descricao, 'Periodo': periodo})

print(df.head())