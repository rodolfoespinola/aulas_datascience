import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('matplotlib/titanic.csv')

survived_counts = df['survived'].value_counts()

print(survived_counts)

plt.figure(figsize=(8, 6))

plt.bar(survived_counts.index, survived_counts, color='pink') # Cria um gŕafico de barras usando os índices e os valores do Series survived_counts, onde as barras são coloridas de rosa. O eixo X reprensenta os valores únicos da coluna 'survived' (0 e 1), e o eixo Y representa a contagem de cada valor.

plt.title('Contagem de sobrevientes')
plt.xlabel('Survived (0/1)')
plt.ylabel("Contagem")

plt.show()