message = 'Fire Emblem 7'

print('Um jogo muito bom:', message)
print('Quantos caracteres tem nesse nome?', len(message))
print('Qual o número do jogo?', message[(len(message) - 1)])
print('Qual o nome da franquia?', message[0:(len(message) - 1)])
print('Letras minúsculas:', message.lower())
print('Letras maiúsculas:', message.upper())
print('Quantos "m"s existem nessa frase?', message.count('m'))
print('Em que posição se inicia a palavra "Emblem"?', message.find('Emblem'))
print('Qual o jogo anterior a esse?', message.replace('7', '6'))

saudacao = 'Olá'
nome = 'Samuel'
print(f'{saudacao}, {nome}. Seja bem vindo!')

#mostra os métodos disponíveis para uma variável
# print(dir(message))
# método help (detalha o funcionamento de uma função/método):
# print(help(str.upper))