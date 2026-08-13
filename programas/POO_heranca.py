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