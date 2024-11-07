from Estoque import Estoque
from Loja import Loja

estoque = Estoque()
loja = Loja(estoque)
first = True

while True:
  print("=== LOJA DE BRINQUEDOS ===")
  if (first == True):
    loja.registrar_usuario()
    
  first = False

  print("\nDIGITE A OPERAÇÃO QUE DESEJA REALIZAR:\n1 - CADASTRAR USUÁRIO\n2 - LOGIN\n3 - ADICIONAR BRINQUEDO\n4 - REMOVER BRINQUEDO\n5 - BUSCAR BRINQUEDO\n6 - CRIAR PEDIDO\n7 - HISTÓRICO DE PEDIDOS\n0 - ENCERRAR SISTEMA")
  op = input()

  match op:
    case "1":
      loja.registrar_usuario()

    case "2":
      loja.realizar_login()

    case "3":
      loja.estoque.adicionar_brinquedo()

    case "4":
      loja.estoque.remover_brinquedo()

    case "5":
      loja.estoque.buscar_brinquedo()

    case "6":
      loja.criar_pedido()

    case "7":
      loja.historico_pedidos()

    case "0":
      break

    case _:
      print("Operação inválida, tente novamente.")

    
