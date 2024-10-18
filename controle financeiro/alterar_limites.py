import math

def alterar_limites(controle):
  cont = 0
  
  print("Selecione a catergoria em que deseja alterar o limite:")
  
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