from datetime import datetime
from Despesa import Despesa
from Mes import Mes
from redefine_controle import redefine_controle

def cadastro_de_despesas(lista_meses):
  repetido = False

  while True:
    try:
      data0 = input("Digite a data dessa despesa (DD/MM/AAAA): ")
      data1 = datetime.strptime(data0, "%d/%m/%Y")
      break

    except ValueError:
      print("Data inválida, tente novamente.") 
  
  mes = str(data1.month)
  ano = str(data1.year)

  mes_ano = mes + '/' + ano

  if (len(lista_meses) != 0):
    for i in lista_meses:
      if (mes_ano == i.get_mes_ano()):
        controle = i.get_mes_controle()
        repetido = True
        break
      controle = redefine_controle()
  else:
    controle = redefine_controle()

  conta = 0
  
  print("Selecione a categoria em que deseja cadastrar sua despesa:")
  
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

  while True:
    try:
      valor = float(input("Digite o valor da despesa: "))
      
      if (valor <= 0):
        print("Valor inválido, tente novamente.")
      
      else:
        break

    except ValueError:
      print("Valor inválido, tente novamente.")

  descricao = input("Digite uma breve descrição da despesa: ")

  data1 = data1.strftime("%d/%m/%Y")

  despesa = Despesa(valor, categ_selecionada.get_nome(), data1, descricao)

  categ_selecionada.append_despesas(despesa)

  if (not(repetido)):
    mes = Mes(mes_ano, controle)
    lista_meses.append(mes)

  return lista_meses

    

