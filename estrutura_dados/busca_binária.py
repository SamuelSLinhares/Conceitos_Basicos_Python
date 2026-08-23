''' 
Forma simples e eficiente de para buscar elementos em uma lista
ordenada

Lógica: Abre uma lista no meio, verifica se o que procura já passou,
descarta a metade desnecessária, repete o processo

Assim, para cada vez que o número de dados dobra, o algorítmo só
precisa de mais uma tentativa

'''

def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            return meio #Encontrou!

        elif lista[meio] < alvo:
            esquerda = meio + 1 # Descarta metade esquerda

        else:
            direita = meio - 1 # Descarta metade direita

    return -1 #Caso não encontre

#Exemplo:
nums = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
resultado = busca_binaria(nums, 23)
print(f'Encontrado na posição: {resultado}')