from math import pi

class Quadrilatero():
    def __init__(self):
        self.lados = []
        self.perimetro = 0

    def calcula_perimetro(self):
        for _ in self.lados:
            self.perimetro += _

    def get_info(self):
        return self.lados
    
    def get_perimetro(self):
        return self.perimetro
    
class Circulo():
    def __init__(self, r, ident):
        self.r = r
        self.ident = ident
    
    def calcula_perimetro(self):
        self.perimetro = 2*pi*self.r

    def calcula_area(self):
        self.area = pi*(self.r)**2

    def get_ident(self):
        return self.ident

    def get_info(self):
        return self.r

    def get_perimetro(self):
        return self.perimetro
    
    def get_area(self):
        return self.area
        
    

    
