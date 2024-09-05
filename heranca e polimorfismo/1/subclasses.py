from classes import Funcionario

class Assistente(Funcionario):
    def __init__(self, matricula, salario):
        super().__init__(matricula, salario)

