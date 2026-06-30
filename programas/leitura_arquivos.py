# readlines lê todas as linhas de uma vez e retorna uma lista
#.strip() exclui os espações em branco no início e fim das strings

#with open('arquivos/notas.txt', 'r') as arquivo:
#    for linha in arquivo:
#        linha_limpa = linha.strip()
#        print(linha_limpa)

# exemplo prático
with open("programas/arquivos/notas.txt", "r") as arquivo:
    soma = 0
    contador = 0

    for linha in arquivo:
        temperatura = float(linha.strip())
        soma += temperatura
        contador += 1

    if contador > 0:
        media = soma / contador
        print(f'A temperatura média foi: {media:.1f}°C')