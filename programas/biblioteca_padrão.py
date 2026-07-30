import random
import math
import datetime
import os

##BIBLIOTECA RANDOM##

##número aleatório em um intervalo:
d20 = random.randint(1,20)
##item aleatório em uma lista
classes = ['Arcanista', 'Bárbaro', 'Clérigo', 'Ladino']
escolha = random.choice(classes)
escolhas = random.choices(classes, k=2)
##escolhe n itens de uma lista, sem repeti-los
casas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorteio = random.sample(casas, k=3)
##embaralhar valores de uma lista
posicao = ['primeiro', 'segundo', 'terceiro']
random.shuffle(posicao)

print(d20, escolha, escolhas, sorteio, posicao)

##BIBLIOTECA MATH##

n_inteiro = 25
n_float = 6.3

raiz = math.sqrt(n_inteiro) ##raiz quadrada
arre_cima = math.ceil(n_float) ##arredonda para cima
arre_baixo = math.floor(n_float) ##arredonda para baixo
pi = math.pi ##retorna número de Pi

print(f'{raiz}, {arre_cima}, {arre_baixo}, {pi:.2f}')

##BIBLIOTECA DATETIME##

agora = datetime.datetime.now() ##.year para apenas ano, .month e etc
data_especifica = datetime.datetime(2026, 1, 25, 13, 56, 00)

##Operações com dias
prazo = data_especifica + datetime.timedelta(days=7) 
##Formatando
agora_formatado = agora.strftime("%d/%m/%Y")

print(agora, data_especifica, prazo, agora_formatado)

##BIBLIOTECA OS##

os.getcwd() ##Retorna diretório atual
os.path
