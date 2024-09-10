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