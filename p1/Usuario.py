class Usuario ():
  def __init__(self, nome, endereco, telefone, email, cartao_credito):
    self.nome = nome
    self.endereco = endereco
    self.telefone = telefone
    self.email = email
    self.cartao_credito = cartao_credito
    self.cpf = None
    self.senha = None

  def validar_cpf(self, cpf, usuarios):
    pass

  def definir_senha(self, senha):
    pass

  def get_nome(self):
    return self.nome

  def get_endereco(self):
    return self.endereco

  def get_telefone(self):
    return self.telefone

  def get_email(self):
    return self.email

  def get_cartao_credito(self):
    return self.cartao_credito

  def get_cpf(self):
    return self.cpf

  def get_senha(self):
    return self.senha
  
  def set_cpf(self, cpf):
    self.cpf = cpf

  def set_senha(self, senha):
    self.senha = senha
