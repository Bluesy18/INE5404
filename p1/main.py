from Brinquedo import Brinquedo
from Estoque import Estoque
from Loja import Loja
from Pedido import Pedido
from Usuario import Usuario

estoque = Estoque()
loja = Loja(estoque)
first = True

while True:
  print("=== LOJA DE BRINQUEDOS ===")
  if (first == True):
    loja.registrar_usuario()
    
  first = False

  print("DIGITE A OPERAÇÃO QUE DESEJA REALIZAR:\n1 - CADASTRAR USUÁRIO\n2 - LOGIN\n0 - ENCERRAR SISTEMA")
  op = input()

  match op:
    case "1":
      loja.registrar_usuario()

    case "2":
      loja.realizar_login()

    
