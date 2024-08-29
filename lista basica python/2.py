def info(cont):
    if (cont == 0):
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")
        cont += 1

    else:
        print("Erro, tente novamente.")
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")

    return nome, senha, cont

def verifica0(nome, senha, cont):
    while(nome == senha):
        nome, senha, cont = info(cont)
    return nome, senha, cont

cont = 0

nome, senha, cont = info(cont)
nome, senha, cont = verifica0(nome, senha, cont)

print(nome, senha)
