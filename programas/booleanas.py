# recebe o input do usuário (str) e o converte para float
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

#compara igualdade
if( valor1 == valor2 ):
        print('Os valores são iguais!')
#em caso de não-igualdade, compara os valores
elif( valor1 != valor2 and valor1 > valor2):
        print(f'O valor 1 ({valor1}) é maior que o valor2 ({valor2})!')
else:
        print(f'O valor 2 ({valor2}) é maior que o valor1 ({valor1})!')
    
