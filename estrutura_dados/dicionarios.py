"""
Dicionários são úteis para a leitura de grandes quantidades de dados,
armazenando uma chave para cada dado
"""
##Dicionário vazio, representado por chaves
d = {}

# Dicionário preenchido
alunos = { # As chaves devem ser imutáveis, como int, float, str ou tuple
    "Ana": 8.5, 
    "Bruno": 7.0,
    "Carla": 9.2
}

##OPERAÇÕES BÁSICAS

#Acesso
print(alunos["Ana"]) # Saída 8.5

#Adição e Modificação
alunos["Roberta"] = 6.8 #Se a chave não existe, cria. Se existe, modifica

#Remoção
del alunos["Ana"]

##VERIFICANDO ERROS

#Verificação por if
aluno = "Cecília"
if aluno in alunos:
    print(alunos[aluno])
else:
    print("Aluno não encontrado!")

#Verificação por .get, retorna None ou um valor padrão caso não exista
nota = alunos.get("Cecília")

nota = alunos.get("Cecília", "Aluno não encontrado!")

##MÉTODOS DE ITERAÇÃO
#.keys() - Retorna as chaves
#.values() - Retorna os valores
#.items() - Retorna tuplas (chave, valor), ideal para for

for aluno, nota in alunos.items():
    print(f'O aluno {aluno} tirou {nota} na prova')