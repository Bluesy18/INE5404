from random import choice
class Imovel():
    def __init__(self):
        enderecos = {"Bairro Ipiranga": 300, 
                     "Zanelatto": 400, 
                     "Rodeio": 350, 
                     "Palhoça": 250, 
                     "São Pedro": 200, 
                     "Chico Mendes": 100, 
                     "Trindade": 500 }
        self.endereco = choice(list(enderecos.keys()))
        self.valor = enderecos[self.endereco]

    def get_endereco(self):
        return self.endereco

    def get_valor(self):
        return self.valor
    