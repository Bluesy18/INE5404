from Usuario import Usuario
from Pedido import Pedido
from getpass import getpass

class Loja():
  def __init__(self, estoque):
    self.estoque = estoque
    self.usuarios = []
    self.pedidos = []
    self.usuario_atual = None

  def registrar_usuario(self):
    print("=== REGISTRO DE USUÁRIO ===")

    while True:
      nome = input("Digite seu nome: ")
      
      if (nome.isalpha() == True):
        break
      
      else:
        print("Nome inválido, tente novamente.")

    endereco = input("Digite seu endereço: ")

    while True:
      telefone = input("Digite o telefone (com DDD, 9 na frente e sem espaços ou traços): ")

      if (len(telefone) == 11 and telefone.isdigit()):
        break

      else:
        print("Telefone inválido, tente novamente.")

    while True:
      email = input("Digite seu email: ")
      
      if("@" in email and ".com" in email):
        break
      
      else:
        print("Email inválido, tente novamente.")

    while True:
      cartao_credito = input("Digite os números do seu cartão de crédito: ")

      if (len(cartao_credito) == 16 and cartao_credito.isdigit()):
        break

      else:
        print("Cartão de crédito inválido, tente novamente.")

    usuario = Usuario(nome, endereco, telefone, email, cartao_credito)

    while True:
      cpf = input("Digite seu CPF: ")
      if(usuario.validar_cpf(cpf, self.usuarios)):
        usuario.set_cpf(cpf)
        usuario.info.append(cpf)
        break
      print("CPF inválido, tente novamente.")

    while True:
      senha = input("Digite sua senha: ")
      if(usuario.definir_senha(senha, usuario)):
        usuario.set_senha(senha)
        break
      print("Senha inválida, tente novamente.")

    self.usuarios.append(usuario)

  def realizar_login(self):
    logado = False
    print("=== LOGIN ===")
    while True:
      cpfLogin = input("Digite seu CPF: ")
      senhaLogin = getpass("Digite sua senha: ")
      for i in self.usuarios:
        if(cpfLogin == i.get_cpf() and senhaLogin == i.get_senha()):
          self.usuario_atual = i
          logado = True
          print("Login feito com sucesso.")
          break
      if (logado):
        break
      print("Informações inválidas, tente novamente.")
      
  def criar_pedido(self):
    print("=== PEDIDO ===")

    usuario = self.usuario_atual
    
    if (usuario == None):
      print("Primeiro faça o login.")
      return

    brinquedos = self.estoque.get_brinquedos()
    brinquedos_escolhidos = []
    quantidades = []

    if (not(brinquedos)):
      print("Não há brinquedos no estoque.")
      return 

    while True:
      cont = 0

      print("Brinquedos em estoque:")
      for i in brinquedos:
        print(f"\n{cont} - {i}")
        cont += 1

      while True:
        try:
          brinEsc = int(input("Digite o número correspondente ao brinquedo que deseja pedir: "))
          if (0 <= brinEsc < len(brinquedos)):
            brinquedo_escolhido = brinquedos[brinEsc]
            break
          print("Escolha inválida, tente novamente.")

        except ValueError:
          print("Escolha inválida, tente novamente.")

      while True:
        try:
          quantidade = int(input("Digite a quantidade desse brinquedo que você deseja: "))
          if (quantidade <= brinquedo_escolhido.get_qtd_estoque()):
            brinquedos_escolhidos.append(brinquedo_escolhido)
            quantidades.append(quantidade)
            brinquedo_escolhido.atualizar_estoque(quantidade)
            break
          print("Quantidade inválida, tente novamente.")

        except ValueError:
          print("Quantidade inválida, tente novamente.")

  
      rep = input("Deseja pedir outro brinquedo? Se sim, digite S: ").upper()
      
      match rep:
        case "S":
          None
        case _:
          pedido = Pedido(usuario, brinquedos, brinquedos_escolhidos, quantidades)
          pedido.calcular_total()
          self.pedidos.append(pedido)
          break

  def historico_pedidos(self):
    print("=== HISTÓRICO DE PEDIDOS ===")
    for i in self.pedidos:
      print(i)

      


  