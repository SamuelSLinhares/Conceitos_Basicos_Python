from collections import deque

'''
Diferentemente de strings, listas são mutáveis!
'''

nums = [42, 123, 33, 67, 89, 00]
nums[1] = 45 #O valor 123, é substituído por 45 na memória

##Verificando pertinência
45 in nums #Retorna True!

##PERCORRENDO UMA LISTA

#Iteração Simples (apenas leitura):
for num in nums:
    print(num)

#Iteração com Índices
for i in range(len(nums)):
    nums[i] = nums[i] * 2

## OPERAÇÕES COM LISTAS

#Concatenação
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b #[1, 2, 3, 4, 5, 6]

#Repetição
a3 = a * 3 #[1, 2, 3, 1, 2, 3, 1, 2, 3]

##FATIAS DE LISTA

#Extração de Sublistas
t = ['a', 'b', 'c', 'd', 'e', 'f']
u = ['a', 'b', 'c', 'd', 'e', 'f']
v = ['a', 'b', 'c', 'd', 'e', 'f']
t2 = t[1:3] #Do índice 1 até o 3 (não inlcui o 3)
u2 = u[:4] #Início até o 4 (não inclui o quatro)
v2 = v[3:] #Ìndice 3 até o final
print(t2, u2, v2)

#Modificando através de fatias
t[1:3] = ["x", "y"]

##MÉTODOS DE LISTA
t.append("g") #Adiciona o elemento ao final da lista
t.sort() #Organiza em ordem crescente
t.extend(c) #Adiciona todos os elementos de c em t
print(t)
sum(c) #Soma os elementos

##Excluir Elementos
t.pop(1) #Remove e retorna por índice
t.pop() #Sem índice específico, exclui e retorna o último

del(t[2]) #Remove sem retornar

c.remove(2) #Remove por valor, apenas o primeiro

##Listas e Strings
palavra = "ventilador"
list(palavra) #Transforma a string em uma lista

frase = "Dormir de ventilador ligado"
lista_frase = frase.split() #Separa as palavras e adiciona na lista

delimiter = " "
frase2 = delimiter.join(lista_frase) #Pega uma lista de strings e 
                    #Concatena em uma única string

a = [1, 2, 3]
b = a ##Agora b referencia a, alterações feitas a um afetam o outro

##LISTA ENCANDEADA (LINKED LIST)
'''
Arrays exigem memória vizinha (contínua). Linked lists aceitam 
memória espalhada (fragmentada)

Arrays são mais vantajosos para velocidade de leitura, no entanto,
Linked Lists se destacam na velocidade de gravação

Python não possue Linked List nativas, mas existe a estrutura deque,
uma Doubly Linked List

'''
#cria a lista
playlist = deque(['Música 1', 'Música 2', 'Músca 3'])

#Inserção Flash no início (O(1))
#Em uma lista normal, esse processo seria lento

playlist.appendleft('Música Nova')

#Removendo do final
playlist.pop()

print(playlist)