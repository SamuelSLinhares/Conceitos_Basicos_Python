while True:
    escolha = int(input('O que você deseja fazer?\n(1) Fornecer um número máximo para contagem\n(2) Fornecer uma palavra para extração de letras\n(3) Ver que números são pares entre 1 e o número fornecido\n(4) Sair do programa\n'))

    if escolha == 1:
        num = int(input('\nAté que número você quer contar? '))
        i = 1
        while i <= num:
            print(i)
            i += 1
        
    elif escolha == 2:
        palavra = input('\nQue palavra você deseja utilizar? ')
        
        for letra in palavra:
            print(letra)

    elif escolha == 3:
        num_max = int(input('\nQual o valor máximo a ser verificado? '))
        numeros = []
        
        for i in range(num_max):
            numeros.append(i+1)

        for n in numeros:
            if n % 2 != 0:
                continue
            print(f'O número {n} é par!')

    elif escolha == 4:
        print('O programa será encerrado.')
        break

    else:
        print('\nOpção inválida, tente novamente!\n')
    
    print('')