from abc import ABC, abstractmethod
import math

class Pessoa(ABC): ##Abstração, pois não há necessidade de guardar uma "pessoa genérica"
    def __init__(self, nome, cpf): ##inicializa a classe ao ser chamada
        self._nome = nome # _ = Protegido
        self.__cpf = cpf #__ = Privado (encapsulado)

    #Define que toda pessoa deve saber se apresentar, deixando a
    #implantação específica para as filhas
    
    @abstractmethod
    def apresentar(self):
        pass

    def get_cpf_mascarado(self):
        return f'***.{self.__cpf[4:7]}.***-**'


class Professor(Pessoa): #Herda características de Pessoa
    def __init__(self, nome, cpf, disciplina):
        super().__init__(nome, cpf)
        self.disciplina = disciplina

    ##implementação obrigatóra do método abstrato
    def apresentar(self):
        print(f'Bom dia, sou o Professor {self._nome} de {self.disciplina}')

class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula):
        super().__init__(nome, cpf)
        self.matricula = matricula

    def apresentar(self):
        print(f'Olá, sou o aluno {self._nome} (Matrícula: {self.matricula})')

professores = []
alunos = []
continuar = True

while continuar:
    escolha = int(input("O que você deseja fazer?\n(1) Cadastrar um professor\n(2) Cadastrar um aluno\n(3) Iniciar apresentações\n(4) Fechar Aplicação\n"))

    if escolha == 1:
        nome, cpf, disciplina = input('Digite o nome, cpf, e a disciplina do professor separados por vírgulas: ').split(', ')
        p = Professor(nome, cpf, disciplina)
        professores.append(p)

    elif escolha == 2:
        nome, cpf, matricula = input('Digite o nome, o cpf, e matrícula do aluno, separados por vírgulas: ').split(', ')
        a = Aluno(nome, cpf, matricula)
        alunos.append(a)

    elif escolha == 3:
        for p in professores:
            p.apresentar()
        for a in alunos:
            a.apresentar()
        
    else:
        continuar = False