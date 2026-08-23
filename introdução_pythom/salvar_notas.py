
with open("programas/arquivos/notas_turma.txt", "w") as arquivo:
    arquivo.write("Notas da Turma\n")
    arquivo.write("=" * 30 + "\n\n")

    try:
        qtd_alunos = int(input('Quantos alunos existem na turma? '))
    except:
        print('Tipo inválido: Digite um número inteiro')
    else:
        for i in range(qtd_alunos):
            nome = input(f'Nome do aluno {i+1}: ')
            nota = input(f'Nota do aluno {i+1}: ')
            arquivo.write(f'{nome}: {nota}\n')

        arquivo.write("\nFim do registro.")
        print("Notas salvas com sucesso!")