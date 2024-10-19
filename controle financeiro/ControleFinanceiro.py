class ControleFinanceiro():
  def __init__(self, categorias):
    self.categorias = categorias
    self.meses = {}

  def get_categorias(self):
    return self.categorias
  
  def get_meses(self):
    return self.meses

  def append_meses(self, mes, despesa):
    self.meses[mes].append(despesa)

  def create_mes(self, mes, despesa):
    self.meses[mes] = [despesa]
    