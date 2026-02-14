from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://quotes.toscrape.com/'
html = urlopen(url)

bs = BeautifulSoup(html, 'html.parser')

linhas = bs.find_all('div', {'class': 'quote'})
'''
outras formas de fazer o mesmo:

O BeautifulSoup permite passar a classe como um argumento nomeado. Como class é uma palavra reservada no Python, usamos class_ (com underline):
linhas = bs.find_all('div', class_='quote')

Método .select() do CSS
linhas = bs.select('div.quote')
'''

frases, autores = [], []

for linha in linhas:
    texto = linha.find('span', class_='text').text # Armazena apenas a string
    nome_autor = linha.find('small', class_='author').text

    frases.append(texto)
    autores.append(nome_autor)

df = pd.DataFrame({'Frase': frases, 'Autor': autores})

print(df.head())

autor_top = df['Autor'].value_counts().idxmax()
print(f'O autor com mais frases nesta paǵina é {autor_top}')

# Contar frases por autor
contagem = df['Autor'].value_counts()

# Gráfico de barras
contagem.plot(kind='bar', color='skyblue', edgecolor='black')

# Personalização
plt.title('Quantidade de frases por Autor')
plt.xlabel('Autores')
plt.ylabel('Número de frases')

# Ajuste layout
plt.tight_layout()

plt.show()