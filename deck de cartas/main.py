from Deck import Deck

deck = Deck()

while True:
  print("\n=== DECK DE CARTAS ===\nEscolha o que deseja fazer\n1 - Mostrar o deck\n2 - Retirar cartas do deck\n3 - Embaralhar o deck\n0 - Encerrar o programa\n")
  op = input()

  match op:
    case "1":
      if (len(deck.get_deck()) == 0):
        print("\nO deck não tem mais nenhuma carta.")

      else:
        print()
        for i in deck.get_deck():
          if (deck.get_deck().index(i) == len(deck.get_deck()) - 1):
            print(i)
          else:
            print(i, end=", ")

    case "2":
      if (len(deck.get_deck()) == 0):
        print("\nNão há mais cartas para serem retiradas.")
      else:
        while True:
          try:
            while True:
              qtd = int(input(f"\nDigite quantas cartas deseja retirar (quantidade atual: {len(deck.get_deck())}): "))
              if (1 <= qtd <= len(deck.get_deck())):

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

    case "3":
      deck.emabaralhar()
      print("\nDeck embaralhado.")

    case "0":
      print("\nEncerrando programa...")
      break

    case _:
      print("\nOpção inválida, tente novamente.")



