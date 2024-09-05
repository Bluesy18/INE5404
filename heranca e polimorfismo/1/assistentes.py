from subclasses import Assistente

class Tec(Assistente): 
    def __init__(self, matricula, salario):
        super().__init__(matricula, salario)

        self.salario = self.salario*1.20



class Admin(Assistente):
    def __init__(self, matricula, salario, turno):
        super().__init__(matricula, salario)

        self.turno = turno
        if(turno == "N"):
            self.salario = self.salario*1.15

    def get_turno(self):
        return self.turno

        
        