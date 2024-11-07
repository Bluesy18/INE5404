class Estoque():
  def __init__(self):
    self.brinquedos = []

  def adicionar_brinquedo(self, novo_brinquedo):
    self.brinquedos.append(novo_brinquedo)

  def remover_brinquedo(self, brinquedo_retirado):
    self.brinquedos.remove(brinquedo_retirado)

  def buscar_brinquedo(self, nome_brinquedo):
    for _ in self.brinquedos:
      if (nome_brinquedo == _.get_nome()):
        print(_)
        break

  