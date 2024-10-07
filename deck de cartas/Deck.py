# Importação da biblioteca datetime para auxiliar na geração de um número pseudo-aleatrório
from datetime import datetime

# Criação da classe Deck
class Deck():
  def __init__(self):
    # Criação de um deck padrão com 52 cartas
    self.numeros = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    self.naipes = ["♥", "♦", "♣", "♠"]
    self.deck = []

    for i in self.numeros:
      for j in self.naipes:
        self.carta = i+j
        self.deck.append(self.carta)

    # Criação de lista para informar ao usuário quais cartas foram retiradas do baralho
    self.retiradas = []


  # Método para embaralhar o deck
  def emabaralhar(self):
    # Variável que armazena o último índice da lista deck
    self.ultimo_index = len(self.deck) - 1

    # Equanto o último índice for maior que 0
    while self.ultimo_index > 0:
      # Gera um número aleatório com base nos microsegundos do instante atual fazendo a operação mod com o último index (assim gerando um número entre 0 e último_index-1)
      self.aleatorio = datetime.now()
      self.index_aleatorio = self.aleatorio.microsecond % self.ultimo_index
      # Armazena a carta correspondente ao último index da lista
      temp = self.deck[self.ultimo_index]
      # Troca a última carta pela carta com o index aleatório
      self.deck[self.ultimo_index] = self.deck[self.index_aleatorio]
      # E troca a carta com o index aleatório pela última carta
      self.deck[self.index_aleatorio] = temp
      # Decrementa o último index, já que agora a carta que realmente tem o último index já foi embaralhada
      self.ultimo_index -= 1


  # Método para retirar cartas, que tem como parâmetro a quantidade de cartas que serão retiradas
  def pegar_cartas(self, qtd):

    # Por uma quantidade de vezes igual a quantidade de cartas retiradas
    for _ in range(qtd):
      # A carta com index 0 (topo do baralho) é adicionada na lista de retiradas
      self.retiradas.append(self.deck[0])
      # E é retirada da lista deck
      self.deck.pop(0)
    # Retorna a lista de retiradas
    return self.retiradas
  
  # Função que apenas retorna as cartas retiradas
  def get_retiradas(self):
    return self.retiradas

  # Função que retona a lista deck
  def get_deck(self):
    return self.deck
  
