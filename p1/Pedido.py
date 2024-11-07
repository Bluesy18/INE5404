class Pedido ():
  def __init__(self, usuario, brinquedos, brinquedos_escolhidos, quantidades):
    self.usuario = usuario
    self.brinquedos = brinquedos
    self.brinquedos_escolhidos = brinquedos_escolhidos
    self.quantidades = quantidades
    self.total = 0.0

  def __str__(self):
    relatList = []
    for i in range(len(self.quantidades)):
      relatList.append((self.brinquedos_escolhidos[i].get_nome()) + " " + str(self.quantidades[i]) + "x")

    relat = ', '.join(relatList)

    return f"Usuário: {self.usuario.get_nome()}\nPedidos: {relat}\nTotal: R${self.total}\n"

  def calcular_total(self):
    for i in range(len(self.quantidades)):
      self.total += (self.brinquedos_escolhidos[i].get_preco()*self.quantidades[i])

  