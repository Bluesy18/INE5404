from Usuario import Usuario

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
    pass

  def criar_pedido(self):
    pass
  