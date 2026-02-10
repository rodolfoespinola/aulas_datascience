import matplotlib.pyplot as plt

x = ['Ricardo', 'Ana', 'Denilson', 'Gabriela']
y = [3200, 5000, 2350, 7500]

plt.bar(x, y, color = 'red')

plt.xlabel('Funcinário')
plt.ylabel('Salário')
plt.title('Proporção salarial')

plt.show()