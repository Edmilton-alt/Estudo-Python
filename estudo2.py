#Loops (repetição)
for i in range(5):
    print("Hello World!")

#Uso de teste
arma=["espada", "glock", "katana", "machado"]
usavel=["escudo","poção","pokebola"]
inventario = arma + usavel

print("Você tem esses itens: ")
print(inventario)

for item in inventario:
    if item in arma:
        print("Esse item é uma arma")
    else:
        print("Esse item é usável")
