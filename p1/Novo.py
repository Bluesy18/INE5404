from Brinquedo import Brinquedo

class Novo(Brinquedo):
  def __init__(self, nome, preco, faixa_etaria, qtd_estoque):
    super().__init__(nome, preco, faixa_etaria, qtd_estoque)
    self.preco = self.preco*1.10
