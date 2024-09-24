# SUV, Econômico, Compacto, Luxo

class Veiculo():
    def __init__(self, placa, cor, marca, modelo, ano, status):
        self.placa = placa
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.status = status
        self.valor = None

    def get_placa(self):
        return self.placa
    
    def get_cor(self):
        return self.cor
    
    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return self.modelo 
    
    def get_ano(self):
        return self.ano
        
    def get_status(self):
        return self.status
    
    def get_valor(self):
        return self.valor
    