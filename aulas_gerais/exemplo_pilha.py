pilha = [];
pilha.append(1) # adiciona o elemento 1 no topo da pilha
pilha.append(2)
pilha.append(3)
print(pilha)
pilha.pop() # remove o último elemento a entrar na pilha
print(pilha)

# Exemplo fila
from collections import deque
fila = deque()
fila.append(1) # adiciona o elemento 1 no final da fila
fila.append(2)
fila.append(3)
print(fila)
fila.popleft() # remove o primeiro elemento a entrar na fila
print(fila)