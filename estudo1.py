#Condições
print("Pontos pra ganha: 2000")
pontos = int(input("Quantos pontos você conseguiu? "))
meta = 2000

if pontos > meta:
    print("Passou de nível!")
    bonus=pontos*0.1
    print(f"ganhou bônus de +{bonus} de xp")
elif pontos == meta:
    print("Passou de nível!")
    print("não ganhou bônus :(")
else:
    print("Não passou de nível")

#Lista
inventario=["espada", "escudo", "poção", "mapa"]
item=input("Qual item você procura? ").lower()

if item in inventario:
    print(f"{item} está no seu inventário!")
else:
    print(f"{item} não foi encontrado(a) no inventário")

