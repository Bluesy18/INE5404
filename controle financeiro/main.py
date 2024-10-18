from Despesa import Despesa
from Categoria import Categoria
from ControleFinanceiro import ControleFinanceiro
from Usuario import Usuario
from cadastro_de_usuario import cadastro_de_usuario
from alterar_limites import alterar_limites
import math

educacao = Categoria("Educação")
energia = Categoria("Energia")
agua = Categoria("Água")
internet = Categoria("Internet")
alimentacao = Categoria("Alimentação")
transporte = Categoria("Transporte")
residencia = Categoria("Residência")
entretenimento = Categoria("Entretenimento")

controle = ControleFinanceiro({educacao.get_nome(): educacao,
                               energia.get_nome(): energia,
                               agua.get_nome(): agua,
                               internet.get_nome(): internet,
                               alimentacao.get_nome(): alimentacao,
                               transporte.get_nome(): transporte,
                               residencia.get_nome(): residencia,
                               entretenimento.get_nome(): entretenimento,})

first = True

while True:
  print("=== SISTEMA DE CONTROLE FINANCEIRO ===")
#  if (first == True):
#    usuario = Usuario(*cadastro_de_usuario())
  
  first = False

  print("DIGITE A OPERAÇÃO QUE DESEJA REALIZAR:\n1 - ALTERAR LIMITES\n0 - ENCERRAR SISTEMA")
  op = input()

  match op:
    
    case "1":
      alterar_limites(controle)

    case "0":
      print("Encerrando sistema...")
      break

    case _:
      print("Operação inválida, tente novamente.")

    

  
  


