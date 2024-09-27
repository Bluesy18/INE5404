from random import randint

class Coffee():
  def __init__(self):
    self.cheio = True

  def drink(self):
    self.cheio = False

  def refill(self):
    self.cheio = True

class Thiago():
  def __init__(self):
    self.isHappy = True

class Codigo():
  def __init__(self):
    self.erros = 0

  def erro(self):
    self.erros += 1

  def debugar(self):
    self.erros = 0

  def programar(self):
    e = randint(0, 1)
    if (e == 1):
      self.erro()

thiago = Thiago()
cafe = Coffee()
codigo = Codigo()

while (cafe.cheio and thiago.isHappy):
  # Programar
  codigo.programar()

  # Debugar
  if(codigo.erros > 0):
    thiago.isHappy = False
    codigo.debugar()

  # Beber café
  cafe.drink()
  thiago.isHappy = True

  # Repetir
  if(cafe.cheio == False):
    cafe.refill()




  


