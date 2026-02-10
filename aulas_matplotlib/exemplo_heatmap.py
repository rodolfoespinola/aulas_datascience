import matplotlib.pyplot as plt
import seaborn as sns

voos = sns.load_dataset('flights')

voos = voos.pivot(index='month', columns='year', values='passengers')

plt.figure(figsize=(10,6))

sns.heatmap(voos, annot=True, fmt='.0f') # Cria um mapa de calor usando o DataFrame voos, onde os valores são anotados nas células do mapa de calor com formato de número inteiro (sem casas decimais). Annot=True ativa a anotação dos valores nas células, e fmt='.0f' formata os números como inteiros sem casas decimais.

plt.show()