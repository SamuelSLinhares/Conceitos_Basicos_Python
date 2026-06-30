#para arquivos pequenos

with open("notas.txt", 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# para ler linha por linha
# para cada readline chamado, ele pula automaticamente para a próxima linha
with open('notas.txt', 'r') as arquivo:
    primeira_linha = arquivo.readline()
    segunda_linha = arquivo.readline()
    terceira_linha = arquivo.readline()
    print(primeira_linha)
    print(segunda_linha)
    print(terceira_linha)

# readlines lê todas as linhas de uma vez e retorna uma lista
with open('notas.txt', 'r') as arquivo:
    for linha in arquivo:
        linha_limpa = linha.strip()
        print(linha_limpa)

