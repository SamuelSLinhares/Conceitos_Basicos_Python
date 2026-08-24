"""
Enquanto numa lista a posição (índice) define a 
identidade do elemento, em um conjunto, a existência
é o único fator relevante

Um set é definido como uma coleção mutável de
elementos imutáveis e não ordenados

Usa-se set em problemas onde deve-se saber da
existência de um valor 

"""

frutas = {'maçã', 'banana', 'uva'}
lista_bruta = [1, 2, 2, 3, 3, 3, 4, 1]
numeros_unicos = set(lista_bruta)
#numeros únicos armazena apenas {1, 2, 3, 4}

grupo_a = {1, 2, 3}
grupo_b = {3, 1, 2, 1}
sao_iguais = (grupo_a == grupo_b) #True

##OPERAÇÕES BINÁRIAS
a = {1, 2, 3}
b = {2, 3, 4}

itersecao = a & b #{2, 3}
uniao = a | b #{1, 2, 3, 4}
diferenca = a - b #{1}
dif_simetrica = a ^ b #{1, 4}