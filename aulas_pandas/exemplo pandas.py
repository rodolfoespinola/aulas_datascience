import pandas as pd

data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'Idade': [25, 30, 35, 40],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Salvador', 'Brasília']
}

df = pd.DataFrame(data)

print(df)

print(df['Nome'])

# Acessando uma linha
print(df.iloc[0])

# Acessar um valor específico
print(df.loc[0, 'Nome'])