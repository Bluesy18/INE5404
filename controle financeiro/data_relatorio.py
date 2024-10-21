def data_relatório(lista_meses):
  if (len(lista_meses) == 0):
    print("Não há meses cadastrados.")
    return
  
  else:
    print("Selecione o mês que deseja fazer o relatório: ")
    for i in lista_meses:
      print(f"{lista_meses.index(i)} - {i.get_mes_ano()}")

    try:
      while True:
        sel1 = int(input())
        if (0 <= sel1 <= len(lista_meses) - 1):
          mes_rel = lista_meses[sel1]
          break
        else:
          print("Mês inválido, tente novamente.")

    except ValueError:
      print("Mês inválido, tente novamente.")

    print("Selecione com qual mês você deseja fazer a comparação: ")

    for j in lista_meses:
      print(f"{lista_meses.index(j)} - {j.get_mes_ano()}")

    try:
      while True:
        sel2 = int(input())
        if (0 <= sel2 <= len(lista_meses) - 1):
          mes_comp = lista_meses[sel2]
          break
        else:
          print("Mês inválido, tente novamente.")

    except ValueError:
      print("Mês inválido, tente novamente.")

  return mes_rel, mes_comp