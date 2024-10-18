class Despesa():
  
  def __init__(self, valor, categoria, data, descricao):
    self.valor = valor
    self.categoria = categoria
    self.data = data
    self.descricao = descricao

  def get_valor(self):
    return self.valor
  
  def get_categoria(self):
    return self.categoria
  
  def get_data(self):
    return self.data
  
  def get_descricao(self):
    return self.descricao