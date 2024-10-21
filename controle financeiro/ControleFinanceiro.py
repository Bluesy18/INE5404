class ControleFinanceiro():
  def __init__(self, categorias):
    self.categorias = categorias
    self.meses = {}

  def despesas_total(self, mes_ano):
    self.total = 0
    for i in self.meses[mes_ano]:
      for j in i.get_despesas():
        self.total += j.get_valor()

    return self.total

  def get_categorias(self):
    return self.categorias
  
  def get_meses(self):
    return self.meses

  def append_meses(self, mes_ano, categoria):
    self.meses[mes_ano].append(categoria)

  def create_mes(self, mes_ano, categoria):
    self.meses[mes_ano] = [categoria]
    