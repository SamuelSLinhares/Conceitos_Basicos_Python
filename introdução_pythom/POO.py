class Lampada:
    def __init__(self, cor, voltagem):
        self.cor = cor
        self.voltagem = voltagem
        self.ligada = False

    def ligar(self):
        self.ligada = True
        print("Lâmpada Ligada")

    def desligar(self):
        self.ligada = False
        print("Lâmpada desligada")

class Conexao:
    def __init__(self, nome):
        self.nome = nome
        print(f'Conexão {self.nome} aberta')
    
    def __del__(self): #serve para garantir o corte de conexões com arquivos e outras coisas
        print(f'Conexão {self.nome} fechada e recursos liberados')

lampada_sala = Lampada("Branca", 220)
lampada_quarto = Lampada("Amarela", 110)

lampada_sala.ligar()
print(f'A lâmpada da sala é {lampada_sala.cor}')
print(lampada_quarto.ligada, lampada_sala.cor)

c = Conexao("Banco de Dados")
del c

##DUNDER METHODS
#__str__: define como o objeto aparece dentro de um print
#__repr__: representação "oficial" do objeto (para debug)
#__len__: permite usar len(objeto)
#__add__: permite somar objetos com +