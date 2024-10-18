def cadastro_de_usuario():
  while True:
    nome = input("Digite seu nome: ")
    
    if (nome.isalpha() == True):
      break
    
    else:
      print("Nome inválido, tente novamente.")
  
  while True:
    email = input("Digite seu email: ")
    
    if("@" in email and ".com" in email):
      break
    
    else:
      print("Email inválido, tente novamente.")

  return nome, email