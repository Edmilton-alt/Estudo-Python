#Dicionário de produtos
armas = ["espada", "machado", "katana", "glock"]
dano = [100, 135, 200, 9999]

dic_armas = {"espada": 100, "machado": 135, "katana": 200, "glock": 9999}

pesquisa = input("Pesquise a arma: ").lower()

if pesquisa in dic_armas:
    print(f"O dano do(a) {pesquisa} é: {dic_armas[pesquisa]}")
else:
    dano_novo = int(input("Esse item não está no inventário, fale quanto de dano ele dá: "))
    dic_armas[pesquisa] = dano_novo
    
    print("Parabéns, arma registrada, você teve um aumento de 10% de dano em todos seus ataques")

    for arma in dic_armas:
        dic_armas1 = round(dic_armas[arma] * 1.1, 2)
        dic_armas[arma] = dic_armas1

    print(dic_armas)