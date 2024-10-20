def data_relatório(controle):
  if (controle.get_meses() == False):
     print("Não há despesas registradas.")
     return
  
  else:
    print("Selecione o mês no qual você deseja fazer o relatório: ")
    keys = list(controle.get_meses().keys())
    print(keys)
    for i in keys:
      print(f"{keys.index(i)} - {i}")

    while True:
      try:  
        mes_srel = int(input())
        if (0 <= mes_srel <= len(keys) - 1):
           mes_rel = keys[mes_srel]
           break
        
        else:
          print("Mês inválido, tente novamente")
      
      except ValueError:
        print("Mês inválido, tente novamente")

    print("Selecione com qual mês você deseja fazer a comparação: ")

    for j in keys:
      print(f"{keys.index(j)} - {j}")

    while True:
      try:  
        mes_scomp = int(input())
        if (0 <= mes_scomp <= len(keys) - 1):
           mes_comp = keys[mes_scomp]
           break
        
        else:
          print("Mês inválido, tente novamente")
      
      except ValueError:
        print("Mês inválido, tente novamente")

  return mes_rel, mes_comp