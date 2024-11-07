class Brinquedo ():
  def __init__(self, nome, preco, faixa_etaria, qtd_estoque):
    self.nome = nome
    self.preco = preco
    self.faixa_etaria = faixa_etaria
    self.qtd_estoque = qtd_estoque

  def __str__(self):
    return f"\nNome: {self.nome}\nPreço: R${self.preco}\nFaixa etária: {self.faixa_etaria}\nQuantidade em estoque: {self.qtd_estoque}"

  def atualizar_estoque(self, qtd):
    self.qtd_estoque -= qtd

  def get_nome(self):
    return self.nome

  def get_preco(self):
    return self.preco

  def get_faixa_etaria(self):
    return self.faixa_etaria

  def get_qtd_estoque(self):
    return self.qtd_estoque