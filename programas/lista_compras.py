def mostrar_menu(): ##exibe opções ao usuário
    try:
        print("\n=== LISTA DE COMPRAS ===")
        print("1. Ver lista")
        print("2. Adicionar item(s)")
        print("3. Sair")
        return int(input("\nO que você quer fazer? "))
    except ValueError:
        print('O valor inserido não é válido, tente novamente.')
    
def carregar_lista(): ## cria uma variável do tipo lista com os itens do arquivo de lista

    itens = []

    try:
        with open("programas/arquivos/lista_compras.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                itens.append(linha.strip)
    except FileNotFoundError:
        pass

    return itens

def salvar_lista(itens): ## salva a lista de itens no arquivo lista
    with open("programas/arquivos/lista_compras.txt", "w", encoding="utf-8") as arquivo:
        for item in itens:
            arquivo.write(item + "\n")

def exibir_lista(itens): ## mostra os itens, enumerate retorna nome + índice
    if len(itens) == 0:
        print("\nSua lista está vazia!")
    else:
        print("\n=== SUA LISTA DE COMPRAS ===")
        qtd = len(itens)
        for i in range(qtd):
            print(f"{i+1}. {itens[i]}")

def adicionar_item(itens):
    try:
        n = int(input("Quantos itens deseja adicionar? "))
    except ValueError:
        print("Valor inválido, tente novamente.")
    else:
        for i in range(n):
            item = input("Digite o item a ser adicionado: ")
            itens.append(item)
        
        print("Itens adicionador com sucesso!")

lista_compras = carregar_lista()
continuar = True

while continuar:
    
    opção = mostrar_menu()

    if opção == 1:
        exibir_lista(lista_compras)

    elif opção == 2:
        adicionar_item(lista_compras)
        salvar_lista(lista_compras)

    elif opção == 3:
        print("Até logo!")
        continuar = False