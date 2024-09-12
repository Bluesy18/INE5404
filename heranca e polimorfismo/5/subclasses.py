from classes import Quadrilatero

class Retangulo(Quadrilatero):
    def __init__(self, b, h, ident):
        super().__init__()
        self.ident = ident
        self.b = b
        self.h = h
        self.lados = [self.b, self.b, self.h, self.h]

    def calcula_area(self):
        self.area = self.b*self.h
    
    def get_ident(self):
        return self.ident

    def get_area(self):
        return self.area
    

class Quadrado(Quadrilatero):
    def __init__(self, l, ident):
        super().__init__()
        self.ident = ident
        self.l = l
        self.lados = [self.l, self.l, self.l, self.l]
    
    def calcula_area(self):
        self.area = self.l*4
        
    def get_ident(self):
        return self.ident

    def get_area(self):
        return self.area


        
