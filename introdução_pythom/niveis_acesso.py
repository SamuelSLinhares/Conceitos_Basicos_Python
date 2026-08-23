class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial ##dunder define o uso estritamente interno da classe

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor): ##permite alterar com validação
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor Inválido para depósito")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

conta = ContaBancaria("Sam", 300)
continuar = True

while continuar:
    escolha = int(input("Bem vindo(a) à sua conta! O que você deseja fazer?\n(1) Verificar Saldo\n(2) Depositar valor\n(3) Sacar valor\n(4) Fechar\n "))

    if escolha == 1:
        print(conta.get_saldo())
    elif escolha == 2:
        valor = int(input("Qual o valor do depósito? "))
        try:
            conta.depositar(valor)
        except:
            print("Não foi possível continuar")
        print(f'O saldo atual é de {conta.get_saldo()}')
    elif escolha == 3:
        valor = int(input("Qual o valor a ser sacado? "))
        try:
            conta.sacar(valor)
        except:
            pass
    else:
        continuar = False