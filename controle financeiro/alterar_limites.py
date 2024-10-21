import math

def alterar_limites(lista_meses):
  if (len(lista_meses) == 0):
    print("Não há meses cadastrados.")
    return
  
  else:
    print("Selecione o mês que deseja alterar: ")
    for i in lista_meses:
      print(f"{lista_meses.index(i)} - {i.get_mes_ano()}")

    try:
      while True:
        sel = int(input())
        if (0 <= sel <= len(lista_meses) - 1):
          mes_selecionado = lista_meses[sel]
          break
        else:
          print("Mês inválido, tente novamente.")

    except ValueError:
      print("Mês inválido, tente novamente.")

    controle = mes_selecionado.get_mes_controle()

    cont = 0
    
    print("Selecione a categoria em que deseja alterar o limite:")
    
    for key in controle.get_categorias():
      print(f"{cont} - {key}")
      cont += 1
    
    while True:

      try:
        cat = int(input())
        
        if (0 <= cat <= cont-1):
          break
        
        else:
          print("Opção inválida, tente novamente.")
      
      except ValueError:
        print("Opção inválida, tente novamente.")

    cat_selecionada = controle.get_categorias()[list(controle.get_categorias().keys())[cat]]

    if (cat_selecionada.get_limite() == math.inf):
      print(f"A categoria {cat_selecionada.get_nome()} não possui limite.")

    else:
      print(f"Limite atual da categoria {cat_selecionada.get_nome()} é de: {cat_selecionada.get_limite()}")

    try:
      while True: 
        limite = float(input("Digite o novo limite: "))

        if (limite >= 0):
          break

        else:
          print("Limite inválido, tente novamente.")

    except ValueError:
      print("Limite inválido, tente novamente.")

    cat_selecionada.set_limite(limite)