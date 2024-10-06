from datetime import datetime

class Deck():
  def __init__(self):
    self.numeros = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    self.naipes = ["♥", "♦", "♣", "♠"]
    self.deck = []
    self.retiradas = []

    for i in self.numeros:
      for j in self.naipes:
        self.carta = i+j
        self.deck.append(self.carta)


  def emabaralhar(self):
    self.ultimo_index = len(self.deck) - 1
    while self.ultimo_index > 0:
      self.aleatorio = datetime.now()
      self.index_aleatorio = self.aleatorio.microsecond % self.ultimo_index
      temp = self.deck[self.ultimo_index]
      self.deck[self.ultimo_index] = self.deck[self.index_aleatorio]
      self.deck[self.index_aleatorio] = temp
      self.ultimo_index -= 1

  def pegar_cartas(self, qtd):
    for _ in range(qtd):
      self.retiradas.append(self.deck[0])
      self.deck.pop(0)

    return self.retiradas
  
  def get_retiradas(self):
    return self.retiradas

  def get_deck(self):
    return self.deck
  
