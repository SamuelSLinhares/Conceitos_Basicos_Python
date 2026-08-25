"""

Uma Tupla é uma estrutura de dados imutável e ordenada, sendo um dado
de somente leitura; A ordem dos elementos é preservada rigorosamente.

Ocupam menos espaço que listas e possuem capacidade de Hash, tornando-as
usaveis como chaves em dicionários ou itens em conjuntos set;


"""

dados_do_usuario = ("Alice", 25, "Engenheira")

nome = dados_do_usuario[0] # Alice
idade = dados_do_usuario[1] # 25

##INDICAR TUPLA MESMO COM UM ITEM
tupla_correta = ("item",) #Reconhecido como tupla
apenas_texto = ("item") #Salvo apenas como str

##CONTAGEM E LOCALIZAÇÃO
dados = (10, 20, 10, 30)

print(dados.count(10)) #Saída: 2
print(dados.index(30)) #Saída: 3