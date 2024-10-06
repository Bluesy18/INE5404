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

    def __str__(self):
        return f"\nINFOS DO VEÍCULO:\nMarca do veículo: {self.get_marca()}\nModelo do veículo: {self.get_modelo()}\nCor do veículo: {self.get_cor()}\nAno de fabricação: {self.get_ano()}\nPlaca do veículo: {self.get_placa()}\nStatus: {self.get_status()}\n"

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
    
    def set_disponivel(self):
        self.status = "Disponível"
    
    def set_alugado(self):
        self.status = "Alugado"

    def set_manutencao(self):
        self.status = "Em manutenção"
    
class Cliente():
    def __init__(self, nome, cpf, telefone, idade, email, cnh):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.idade = idade
        self.email = email
        self.cnh = cnh
        self.historico = []

    def __str__(self):
        return f"\nINFOS DO CLIENTE:\nNome do cliente: {self.get_nome()}\nCPF do cliente: {self.get_cpf()}\nTelefone do cliente: {self.get_telefone()}\nIdade do cliente: {self.get_idade()}\nEmail do cliente: {self.get_email()}\nCNH do cliente: {self.get_cnh()}\nHistórico do cliente: {self.get_historico()}\n"

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
    
    def get_historico(self):
        if (len(self.historico) == 0):
            return "Vazio"
        return self.historico

    def set_historico(self, modelo, retirada, devolucao):
        self.historico.append(f"{modelo} - {retirada} - {devolucao}")
  
class Aluguel():
    def __init__(self, cliente, veiculo, retirada, devolucao, km_inicial):
        self.cliente = cliente
        self.veiculo = veiculo
        self.retirada = retirada
        self.devolucao = devolucao
        self.km_inicial = km_inicial
        self.pagamento = "Pendente"

        formato = "%d/%m"  
    
        self.retirada2 = datetime.strptime(self.retirada, formato)
        self.devolucao2 = datetime.strptime(self.devolucao, formato)
    
        self.diferenca = abs((self.devolucao2 - self.retirada2).days)

        self.valor_total = (self.veiculo.get_valor()*(self.diferenca+1))

    def __str__(self):
        return f"\nINFOS DO CLIENTE:\nNome do cliente: {self.cliente.get_nome()}\nCPF do cliente: {self.cliente.get_cpf()}\nTelefone do cliente: {self.cliente.get_telefone()}\nIdade do cliente: {self.cliente.get_idade()}\nEmail do cliente: {self.cliente.get_email()}\nCNH do cliente: {self.cliente.get_cnh()}\nHistórico do cliente: {self.cliente.get_historico()}\n\nINFOS DO VEÍCULO:\nMarca do veículo: {self.veiculo.get_marca()}\nModelo do veículo: {self.veiculo.get_modelo()}\nCor do veículo: {self.veiculo.get_cor()}\nAno de fabricação: {self.veiculo.get_ano()}\nPlaca do veículo: {self.veiculo.get_placa()}\n\nINFOS DO ALUGUEL:\nRetirada: {self.retirada}\nDevolução: {self.devolucao}\nValor total: {self.valor_total}\nStatus do pagamento: {self.pagamento}\n"

    def get_km_inicial(self):
        return self.km_inicial

    def get_retirada(self):
        return self.retirada
    
    def get_devolucao(self):
        return self.devolucao

    def get_valor_total(self):
        return self.valor_total
    
    def get_pagamento(self):
        return self.pagamento

    def set_pagamento(self):
        self.pagamento = "Pago"

class SistemaAluguel:
    def __init__(self, clientes, veiculos, alugueis):
        self.receita = 0
        self.clientes = clientes
        self.veiculos = veiculos
        self.alugueis = alugueis

    def append_clientes(self, cliente):
        self.clientes.append(cliente)

    def append_veiculos(self, veiculo):
        self.veiculos.append(veiculo)

    def append_alugueis(self, aluguel):
        self.alugueis.append(aluguel)    

    def get_receita(self):
        return self.receita
    
    def set_receita(self, receita):
        self.receita += receita

    

    
    

    