class Categoria():
  
  def __init__(self, nome, limite):
    self.nome = nome
    self.limite = limite
    self.despesas = []

  def get_nome(self):
    return self.nome
  
  def get_limite(self):
    return self.limite
  
  def get_despesas(self):
    return self.despesas