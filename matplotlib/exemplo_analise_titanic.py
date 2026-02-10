import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('matplotlib/titanic.csv') # Precisei colocar o endereço

print(df.head())

print(df.info())

print(df.describe()) # Estatística descritiva. Média da coluna, elementos de coluna

# Datatype
print(df.dtypes)

# Filtro
print(df[df['age'] <= 10].head())

# Limpeza de dados duplicados
duplicateRows = df[df.duplicated()]
print(len(duplicateRows)) # len captura a quantidade de ítens duplicados

# Remoção de linhas duplicadas
print(len(df))
df.drop_duplicates(keep='last', inplace=True) # keep mantenha a última ocorrencia da deuplicação. inplace salva as alterações
print(len(df)) # Só para testar quanto foi apagado

# Remocendo valores nulos do dataframe

# df.dropna(subset=['age'], inplace=True)

df.replace(np.nan, 0, inplace=True) # Subsituindo NaN por 0
print(df)

# Renomear colunas
df = df.rename(columns={'sex': 'Genero'})

print(df.head(5))

sorted_df = df.sort_values(by='Genero', ascending=False)
print(sorted_df)

#groupby
grouped_by = df.groupby('age') # Agrupa os dados por idade, criando um objeto de agrupamento que pode ser usado para realizar operações de agregação ou análise em cada grupo de idade.
print(grouped_by.head())