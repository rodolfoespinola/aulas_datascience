import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic') # Dataset do próprio seaborn

df_por_sexo = titanic.groupby('sex')['survived'].sum().reset_index() # Agrupa os dados por sexo e soma o número de sobreviventes, depois reseta o índice para transformar o resultado em um DataFrame.

plt.figure(figsize=(8,6)) # Define o tamanho da figura do gráfico para 8 polegadas de largura e 6 polegadas de altura.

sns.barplot(data=df_por_sexo, x='sex', y='survived') # Cria um gráfico de barras usando o DataFrame df_por_sexo, onde o eixo x representa o sexo e o eixo y representa o número de sobreviventes.

plt.show()