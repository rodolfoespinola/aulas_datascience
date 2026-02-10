nome = input("Digite seu nome: ")
idade = input("Digite sua idade:")
anonasc = 2026 - int(idade)
print("Olá, " + nome + "! Em 2030 você terá " + str(2030-anonasc) + " anos.")

# o jeito mais moderno
"""
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: ")) 
print(f"Olá, {nome}! Em 2030 você terá {idade + 4} anos.")
"""

