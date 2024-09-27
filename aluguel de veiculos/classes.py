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
    

    