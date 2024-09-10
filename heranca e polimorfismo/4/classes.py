from random import choice, randint
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

class Ingresso:
    def __init__(self):
        self.valor = float(10.00)

    def get_valor(self):
        return self.valor
    
    def imprimeValor(self):
        print(self.valor)

class Funcionario:
    def __init__(self):
        nomes = ["Davi", "André", "Vamps", "Marraui", "Thiago", "Erick"]
        self.matricula = randint(1, 1000)
        self.nome = choice(nomes)
        self.salario = randint(1200, 5000)
    
    def get_matricula(self):
        return self.matricula
    
    def get_nome(self):
        return self.nome
    
    def get_salario(self):
        return self.salario

class Gerente:
    def __init__(self):
        self

