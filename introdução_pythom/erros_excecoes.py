## NameError -> variável não definida
## TypeError -> operação com tipos de dados incompatíveis
## IndexError -> erro de índice
## FileNotFoundError -> tentar abrir arquivo que não existe
## ValueError -> tentar converter int em algo que não é um número
## ZeroDivisionError -> dividir por zero

def dividir(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Os dois valores precisam ser números.")
    if b == 0:
        raise ValueError('O divisor nao pode ser zero.')
    return a / b

try:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    resultado = dividir(n1, n2)
except ValueError as erro:
    print(f'Valor inválido: {erro}')
except TypeError as erro:
    print(f'Tipo inválido: {erro}')
else:
    print(f'Resultado: {resultado:.2f}')
finally:
    print('Obrigado por utilizar o programa!')

## except: executa linha a identificar um erro genérico ou específico
## else: no contexto de try, executa caso nenhum erro seja identificado
## finally: executa a linha independentemente de erro ou não