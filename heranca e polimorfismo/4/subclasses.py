from classes import Ingresso

class VIP(Ingresso):
    def __init__(self):
        super().__init__()
        self.valor = self.valor+10

class Normal(Ingresso):
    def __init__(self):
        super().__init__()

    def normal(self):
        print("Ingresso Normal")

from classes import Funcionario

class Assistente(Funcionario):
    def __init__(self):
        super().__init__()

from classes import Imovel

class Novo(Imovel):
    def __init__(self):
        super().__init__()
    
        self.acrescimo = self.valor*0.05
        self.valor = self.valor + self.acrescimo

    def get_acrescimo(self):
        return self.acrescimo
    
class Velho(Imovel):
    def __init__(self):
        super().__init__()

        self.desconto = self.valor*0.15
        self.valor = self.valor - self.desconto

    def get_desconto(self):
        return self.desconto



