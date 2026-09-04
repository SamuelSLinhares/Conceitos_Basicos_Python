ddd_cadastrados = [61, 71, 11, 21, 32, 19, 27, 31]

ddd_cidades = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

ddd = int(input())

if ddd in ddd_cadastrados:
    print(ddd_cidades[ddd])
else:
    print("DDD nao cadastrado")