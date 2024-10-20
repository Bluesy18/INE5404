import math

class Categoria():

  def __init__(self, nome):
    self.nome = nome
    self.limite = math.inf
    self.despesas = []

  def despesas_total(self):
    self.total = 0
    for _ in self.despesas:
      self.total += _.get_valor()

    return self.total

  def get_nome(self):
    return self.nome
  
  def get_limite(self):
    return self.limite
  
  def get_despesas(self):
    return self.despesas
  
  def set_limite(self, limite):
    self.limite = limite

  def append_despesas(self, despesa):
    self.despesas.append(despesa)

  