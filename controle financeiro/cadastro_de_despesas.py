from datetime import datetime
from Despesa import Despesa

def cadastro_de_despesas(controle):
  conta = 0
  
  print("Selecione a catergoria em que deseja alterar o limite:")
  
  for key in controle.get_categorias():
    print(f"{conta} - {key}")
    conta += 1
  
  while True:

    try:
      categ = int(input())
      
      if (0 <= categ <= conta-1):
        break
      
      else:
        print("Opção inválida, tente novamente.")
    
    except ValueError:
      print("Opção inválida, tente novamente.")

  categ_selecionada = controle.get_categorias()[list(controle.get_categorias().keys())[categ]]

  try:
    while True:
      valor = float(input("Digite o valor da despesa: "))
      
      if (valor <= 0):
        print("Valor inválido, tente novamente.")
      
      else:
        break

  except ValueError:
    print("Valor inválido, tente novamente.")

  while True:
    try:
      data0 = input("Digite a data dessa despesa (DD/MM/AAAA): ")
      data1 = datetime.strptime(data0, "%d/%m/%Y")
      break

    except ValueError:
      print("Data inválida, tente novamente.") 
  
  mes = data1.month

  descricao = input("Digite uma breve descrição da despesa: ")

  despesa = Despesa(valor, categ_selecionada.get_nome(), data1, descricao)

  categ_selecionada.append_despesas(despesa)

  if (mes in controle.get_meses().keys()):
    controle.append_meses(mes, despesa)

  else:
    controle.create_mes(mes, despesa)
