class Pedido ():
  def __init__(self, usuario, brinquedos, brinquedos_escolhidos, quantidade):
    self.usuario = usuario
    self.brinquedos = brinquedos
    self.brinquedos_escolhidos = brinquedos_escolhidos
    self.quantidade = quantidade
    self.total = 0

  def calcular_total(self):
    for i in range(len(self.quantidade)):
      self.total += (self.brinquedos_escolhidos[i].get_preco()*self.quantidade[i])

  