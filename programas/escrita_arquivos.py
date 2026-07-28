## método Write: apaga todo o conteúdo prévio e escreve
with open("programas/arquivos/mensagem.txt", "w") as arquivo:
    arquivo.write("Testando o método Write!\n")
    arquivo.write("Quebra de linha deve ser adicionada manualmente!")

## método Append: adiciona ao final
with open("programas/arquivos/mensagem.txt", "a") as arquivo:
    arquivo.write("\nTestando o método Append!")

