import numpy as np

arr2 = np.array([
    [1, 2, 3], # Aqui é linha 0
    [4, 5, 6], # Aqui é linha 1.
    [7, 8, 9]
])

print(arr2[1, 2])

# Informações da matriz
print(f"Shape da matriz: {arr2.shape}")
print(f"Número de elementos: {arr2.size}")
print(f"Tipo dos elementos: {arr2.dtype}")

# Operações matemáticas

arr1 = np.array([10, 50, 60, 40, 80])

print(arr1 + 10)

print(arr2 * 2)

print('Média')
print(np.mean(arr1))

print('Mediana') # A mediana é o valor que separa a metade superior da metade inferior dos dados. Se o número de elementos for ímpar, a mediana é o valor do meio. Se for par, a mediana é a média dos dois valores centrais.
print(np.median(arr1))

print("Desvio Padrão") # O desvio padrão é uma medida de dispersão que indica o quanto os valores de um conjunto de dados estão espalhados em relação à média. Um desvio padrão baixo indica que os valores estão próximos da média, enquanto um desvio padrão alto indica que os valores estão mais dispersos.
desvio_padrao = np.std(arr1)
print(desvio_padrao)

print("Variância") # A variância é uma medida de dispersão que indica o quanto os valores de um conjunto de dados estão espalhados em relação à média. A variância é calculada como a média dos quadrados das diferenças entre cada valor e a média. Um valor de variância baixo indica que os valores estão próximos da média, enquanto um valor de variância alto indica que os valores estão mais dispersos.
variancia = np.var(arr1)
print(variancia)

min = np.min(arr1)
max = np.max(arr1)

print(f"Mínimo: {min}")
print(f"Máximo: {max}")