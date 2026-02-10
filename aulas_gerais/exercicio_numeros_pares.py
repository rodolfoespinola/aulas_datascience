try:
    # Captura os valores de início e fim da faixa
    inicio = int(input("Digite o início do intervalo: "))
    fim = int(input("Digite o fim do intervalo: "))

    #Garante o funcionamento mesmo se o usuário digitar o intervalo invertido
    num_menor = min(inicio, fim) # Identifica o menor número
    num_maior = max(inicio, fim) # Identifica o maior número

    print(f"Números pares entre {num_menor} e {num_maior}:")

    #Ajusta o primeiro número para que seja par
    if num_menor % 2 != 0:
        num_menor += 1
    
    for i in range(num_menor, num_maior + 1, 2): # Incrementa de 2 em 2 para pegar apenas os pares
        print(i)
except ValueError:# Trata erro de conversão para inteiro
    print("Por favor, insira números inteiros válidos.")
    