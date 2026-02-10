import matplotlib.pyplot as plt

#Criando gráfico de linhas
# plt.plot([1, 3, 5], [2, 6, 7])

# plt.show()

# Dados'
x = ['Maçã', 'Laranja', 'Uva', 'Banana', 'Figos']
y = [5, 3, 7, 4, 6] # Quantidade de ítens do eixo x

plt.bar(x, y, color = 'green')

# Adicionando rótulos
plt.xlabel('Frutas')
plt.ylabel('Quantidade')
plt.title('Quantidade de frutas')

plt.show()