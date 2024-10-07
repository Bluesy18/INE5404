# Importa a classe Deck do arquivo Deck
from Deck import Deck

# Cria objeto deck
deck = Deck()

while True:
  # Menu de operações
  print("\n=== DECK DE CARTAS ===\nEscolha o que deseja fazer\n1 - Mostrar o deck\n2 - Retirar cartas do deck\n3 - Embaralhar o deck\n0 - Encerrar o programa\n")
  op = input()

  match op:

    # Mostrar o deck
    case "1":
      # Caso o deck não tenha cartas, informa ao usuário
      if (len(deck.get_deck()) == 0):
        print("\nO deck não tem mais nenhuma carta.")

      # Caso haja, printa as cartas do deck
      else:
        print()
        for i in deck.get_deck():
          if (deck.get_deck().index(i) == len(deck.get_deck()) - 1):
            print(i)
          else:
            print(i, end=", ")

    # Retirar cartas
    case "2":
      # Caso o deck não tenha cartas para serem retiradas, informa ao usuário
      if (len(deck.get_deck()) == 0):
        print("\nNão há mais cartas para serem retiradas.")

      # Caso haja cartas
      else:
        while True:
          try:
            while True:
              # O usuário informa a quantidade de cartas que ele deseja retirar
              qtd = int(input(f"\nDigite quantas cartas deseja retirar (quantidade atual: {len(deck.get_deck())}): "))
              if (1 <= qtd <= len(deck.get_deck())):

                # Retira e printa as cartas que foram retiradas
                for j in deck.pegar_cartas(qtd):
                  if (deck.get_retiradas().index(j) == 0):
                    print(f"\nCartas retiradas: {j}", end=", ")
                  
                  elif(deck.get_retiradas().index(j) == len(deck.get_retiradas()) - 1):
                    print(j)

                  else:
                    print(j, end=", ")

                break
              else:
                print("\nQuantidade inválida, tente novamente")

            break
            
          except ValueError:
            print("\nQuantidade inválida, tente novamente.")

    # Emabaralhar cartas
    case "3":
      # Chama a função de embaralhar e informa ao usuário
      deck.emabaralhar()
      print("\nDeck embaralhado.")

    # Encerra o programa
    case "0":
      print("\nEncerrando programa...")
      break

    case _:
      print("\nOpção inválida, tente novamente.")



