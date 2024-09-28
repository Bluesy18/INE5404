from datetime import datetime

class Veiculo():
    def __init__(self, placa, cor, marca, modelo, ano):
        self.placa = placa
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.status = "Disponível"

        utilitario = ["Strada", "Nivus"]
        suv = ["Taos", "C4 Cactus", "Spin", "2008"]
        intermediario = ["Cronos", "Virtus", "Cobalt"]
        compacto = ["Polo", "Onix", "208", "C3"]
        economico = ["Argo", "Mobi", "Uno", "Ka", "EcoSport", "Gol", ]

        if(self.modelo in utilitario):
            self.valor = 230

        if(self.modelo in suv):
            self.valor = 312

        if(self.modelo in intermediario):
            self.valor = 170

        if(self.modelo in compacto):
            self.valor = 150

        if(self.modelo in economico):
            self.valor = 135

        if(self.modelo == "Cruze"):
            self.valor = 480

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
    
class Cliente():
    def __init__(self, nome, cpf, telefone, idade, email, cnh):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.idade = idade
        self.email = email
        self.cnh = cnh
    
    def get_nome(self):
        return self.nome
    
    def get_cpf(self):
        return self.cpf
    
    def get_telefone(self):
        return self.telefone
    
    def get_idade(self):
        return self.idade
    
    def get_email(self):
        return self.email
    
    def get_cnh(self):
        return self.cnh
    
class Aluguel():
    def __init__(self, veiculo, retirada, devolucao):
        self.veiculo = veiculo
        self.retirada = retirada
        self.devolucao = devolucao
        self.pagamento = "Em espera"

        formato = "%d/%m"  
    
        self.retirada2 = datetime.strptime(self.retirada, formato)
        self.devolucao2 = datetime.strptime(self.devolucao, formato)
    
        self.diferenca = abs((self.devolucao2 - self.retirada2).days)

        self.valor_total = self.veiculo.get_valor()*self.diferenca

    def get_info(self):
        print(f"\nMarca do veículo: {self.veiculo.get_marca()}\nModelo do veículo: {self.veiculo.get_modelo()}\nCor do veículo: {self.veiculo.get_cor()}\nAno de fabricação: {self.veiculo.get_ano()}\nPlaca do veículo: {self.veiculo.get_placa()}\n\nRetirada: {self.retirada}\nDevolução: {self.devolucao}\nValor total: {self.valor_total}\nStatus do pagamento: {self.pagamento}\n")

    def get_valor_total(self):
        return self.valor_total

    
    

    