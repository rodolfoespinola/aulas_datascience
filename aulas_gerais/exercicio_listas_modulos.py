#Exercício

frutas = []
frutas.append("Maçã")
frutas.append("Banana")
frutas.append("Cereja")
frutas.append("Damasco")
frutas.append("Laranja")

print("-----Frutas selecionadas-----")
for fruta in frutas:
    if fruta in ["Maçã", "Laranja"]:
        print(fruta)
print(f"\nLista completa de frutas: {frutas}")