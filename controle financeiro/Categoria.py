import math

class Categoria():

  def __init__(self, nome):
    self.nome = nome
    self.limite = math.inf
    self.ultrapassou = False
    self.valor_total = 0
    self.despesas = []

  def calcula_valor_total(self):
    self.valor_total = 0
    for i in self.despesas:
      self.valor_total += i.get_valor()

    if (self.valor_total > self.limite):
      self.ultrapassou = True

    return self.valor_total

  def get_nome(self):
    return self.nome
  
  def get_limite(self):
    return self.limite
  
  def get_despesas(self):
    return self.despesas
  
  def get_ultrapassou(self):
    return self.ultrapassou
  
  def set_limite(self, limite):
    self.limite = limite

  def append_despesas(self, despesa):
    self.despesas.append(despesa)

  

  