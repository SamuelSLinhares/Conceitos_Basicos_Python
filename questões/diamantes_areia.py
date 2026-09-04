casos = int(input())

for i in range(casos):
    elementos = input()
    lista_elementos = list(elementos)
    possivel = True

    num = 0
    while possivel:

        if "<" in lista_elementos and ">" in lista_elementos:
            lista_elementos.remove("<")
            lista_elementos.remove(">")
            num += 1
        else:
            possivel = False 

    print(num)

    ##Adicionar verificação da ordem, pois o diamante
    ##só se forma com "<>" e não "><"