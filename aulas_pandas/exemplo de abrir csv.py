import pandas as pd

# Comando para acessar planilha
df = pd.read_csv('exemplo.csv')

# df = pd.read_csv('/caminho/para/o/diretorio/exemplo.csv')

print(df.head()) # Printa as primeiras linhas