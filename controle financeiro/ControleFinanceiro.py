class ControleFinanceiro():
  def __init__(self, categorias):
    self.categorias = categorias
    self.meses = {}

  def get_categorias(self):
    return self.categorias
  
  def get_meses(self):
    return self.meses

  def append_meses(self, mes_ano, despesa):
    self.meses[mes_ano].append(despesa)

  def create_mes(self, mes_ano, despesa):
    self.meses[mes_ano] = [despesa]
    