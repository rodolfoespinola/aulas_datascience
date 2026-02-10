def pure_increments(elements,index):
    new_elements = elements.copy() # Cria uma cópia da lista para evitar modificar a original
    new_elements[index] += 1
    return new_elements

lista = [1, 2, 3, 4, 5  ]

print(pure_increments(lista, 0))

print(lista) 