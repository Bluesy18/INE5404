from classes import Cliente

def cadastro_clientes():
    print("=== CADASTRO DE CLIENTES ===")

    nome = input("Digite o nome: ")

    while True:
        cpf = input("Digite o CPF (sem pontos ou traços): ")

        if (len(cpf) == 11 and cpf.isdigit()):
            break

        else:
            print("CPF inválido, tente novamente.")

    while True:
        telefone = input("Digite o telefone (com DDD, 9 na frente e sem espaços ou traços): ")

        if (len(telefone) == 11 and telefone.isdigit()):
            break

        else:
            print("Telefone inválido, tente novamente.")

    while True:
        try:
            idade = int(input("Digite a idade (mínimo 21): "))

            if (idade >= 21):
                break

            else:
                print("Idade insuficiente para alugar um carro.")

        except ValueError:
            print("Idade inválida, tente novamente.")

    while True:
        email = input("Digite o email: ")

        if("@" in email and ".com" in email):
            break

        else:
            print("Email inválido, tente novamente.")

    while True:
        cnh = input("Digite a CNH: ")

        if(len(cnh) == 10 and cnh.isdigit()):
            break

        else:
            print("CNH inválida, tente novamente.")

    clie = Cliente(nome, cpf, telefone, idade, email, cnh)
    return clie