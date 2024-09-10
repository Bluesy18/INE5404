from subclasses import Assistente
from random import randint

class Tec(Assistente): 
    def __init__(self):
        super().__init__()

        self.salario = self.salario*1.20

class Admin(Assistente):
    def __init__(self):
        super().__init__()

        self.turno = randint(1, 2)
        if (self.turno == 2):
            self.trn = "Noturno"
            self.salario = self.salario*1.15

        else:
            self.trn = "Matutino"

    def get_turno(self):
        return self.trn

        
        