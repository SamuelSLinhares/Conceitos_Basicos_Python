from abc import ABC, abstractmethod
import math

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mover(self):
        print(f'{self.modelo} está se movendo')

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        ##chama init de Veiculo para configurar marca e modelo
        super().__init__(marca, modelo)
        ##configura apenas o específico
        self.portas = portas

    def buzinar(self):
        print("Bi bi!")

meu_carro = Carro("Toyota", "Corolla", 4)
meu_carro.mover()
meu_carro.buzinar()
##IMPORTANTE: Python suporta múltiplas heranças

##POLIMORFISMO: Quando uma classe filha sobrescreve uma função da mae

##Sobrescrita
class Moto(Veiculo):
    def mover(self):
        print(f"{self.modelo} está acelerando em duas rodas!")

veiculos = [Carro("Fiat", "Uno", 2), Moto("Honda", "CG")]

for v in veiculos:
    v.mover()

##Sobrecarga: Geralmente não funciona nativamente em python, usa-se parametros padrão ou argumentos variáveis
class Calculadora:
    ##aceita um parâmetro "b" vazio ou não
    def somar(a, b=0):
        return a + b

print(Calculadora.somar(10))
print(Calculadora.somar(10, 20))

##CLASSES ABSTRATAS:
#Classes que não podem gerar instâncias, apenas terem suas características herdadas

class Forma(ABC): #Herdar de ABC torna a classe abstrata
    @abstractmethod
    def area(self): #Define a obrigatoriedade da implementação de area()
        pass

    def descricao(self): #Podem haver metodos normais também
        print("Sou uma forma geométrica")

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

q = Quadrado(4)
c = Circulo(3)

print(f'Área Quadrado: {q.area()}')
print(f'Área Círculo: {c.area():.2f}')
q.descricao()

##INTERFACES
#Convenção para definir métodos necessárias dentro de uma classe sem a necessidade de fornecer implementação de código
#Todos os métodos devem ser abstratos

class IDesenhavel(ABC): #O 'I' no começo é convenção para Interface
    def desenhar(self):
        pass