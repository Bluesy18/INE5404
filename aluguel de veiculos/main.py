from classes import Veiculo, Cliente
import re

def cadastro_veiculos():

    cores = ["Branco", "Cinza", "Prata", "Preto", "Vermelho", "Azul"]
    marcas = ["Fiat", "Ford", "Volkswagen", "Audi", "Chevrolet", "Peugeot", "Citroen"]
    fiatM = ["Strada", "Cronos", "Argo", "Mobi", "Uno", "Toro"]
    fordM = ["Ka", "EcoSport"]
    volksM = ["Gol", "Polo", "Virtus", "Nivus", "Taos"]
    chevroM = ["Cobalt", "Onix", "Spin", "Cruze"]
    peugeotM = ["208", "2008"]
    citroenM = ["C3", "C4 Cactus", "Aircross"]
    audiM = ["A3", "A4", "A5"]
    placa_padrao = r'^[A-Z]{3}-\d{4}$'

    while True:
        print("=== CADASTRO DE CARROS ===")
        while True:

            placa = input("Digite a placa do carro: ")

            if(re.match(placa_padrao, placa)):
                break

            else:
                print("Placa inválida, tente novamente.")

        print(placa)

        while True:
            print("Cores disponíveis: ")
            print(*cores)
            cor = input("Digite a cor do carro: ")

            if (cor in cores):
                break

            else:
                print("Cor inválida, tente novamente")

        print(cor)

        while True:
            print("Marcas disponíveis: ")
            print(*marcas)
            marca = input("Digite a marca do carro: ")

            if (marca in marcas):
                break

            else:
                print("Marca inválida, tente novamente.")

        match marca:
            
            case "Fiat":
                while True:
                    print("Modelos disponíveis: ")
                    print(*fiatM)
                    modelo = input("Digite o modelo do carro: ")
                    if (modelo in fiatM):
                        break
                    else:
                        print("Modelo inválido, tente novamente.")

            case "Ford":
                while True:
                    print("Modelos disponíveis: ")
                    print(*fordM)
                    modelo = input("Digite o modelo do carro: ")
                    if (modelo in fordM):
                        break
                    else:
                        print("Modelo inválido, tente novamente.")

            case "Volkswagen":
                while True:
                    print("Modelos disponíveis: ")
                    print(*volksM)
                    modelo = input("Digite o modelo do carro: ")
                    if (modelo in volksM):
                        break
                    else:
                        print("Modelo inválido, tente novamente.")

            case "Audi":
                while True:
                    print("Modelos disponíveis: ")
                    print(*audiM)
                    modelo = input("Digite o modelo do carro: ")
                    if (modelo in audiM):
                        break
                    else:
                        print("Modelo inválido, tente novamente.")

            case "Chevrolet":
                while True:
                    print("Modelos disponíveis: ")
                    print(*chevroM)
                    modelo = input("Digite o modelo do carro: ")
                    if (modelo in chevroM):
                        break
                    else:
                        print("Modelo inválido, tente novamente.")

            case "Peugeot":
                while True:
                    print("Modelos disponíveis: ")
                    print(*peugeotM)
                    modelo = input("Digite o modelo do carro: ")
                    if (modelo in peugeotM):
                        break
                    else:
                        print("Modelo inválido, tente novamente.")

            case "Citroen":
                while True:
                    print("Modelos disponíveis: ")
                    print(*citroenM)
                    modelo = input("Digite o modelo do carro: ")
                    if (modelo in citroenM):
                        break
                    else:
                        print("Modelo inválido, tente novamente.")

        print(modelo)

        while True:
            ano = int(input("Digite o ano de fabricação do carro (mínimo 2019): "))

            if (ano >= 2019):
                break

            else:
                print("Ano inválido, tente novamente.")

        print(ano)

        while True:
            status = input("Digite se o carro está (D)isponível, (A)lugado ou em (M)anutenção: ").upper()

            match status:
                case "D":
                    break

                case "A":
                    break

                case "M":
                    break

                case _:
                    print("Status inválido, tente novamente.")

        print(status)
        resp = input("Caso queira continuar cadastrando veículos, digite S: ").upper()

        match resp:
            case "S":
                print("Começando novo cadastro...")
            case _:
                break

    veic = Veiculo(placa, cor, marca, modelo, ano, status)
    veiculos.append(veic)

    print(veiculos[0].get_modelo())

def cadastro_clientes():
    while True:
        print("=== CADASTRO DE CLIENTES ===")

        nome = input("Digite o seu nome: ")

        print(nome)

        while True:
            cpf = input("Digite seu CPF (sem pontos ou traços): ")

            if (len(cpf) == 11 and cpf.isdigit()):
                break

            else:
                print("CPF inválido, tente novamente.")

        while True:
            telefone = input("Digite seu telefone (com DDD, 9 na frente e sem espaços ou traços): ")

            if (len(telefone) == 11 and telefone.isdigit()):
                break

            else:
                print("Telefone inválido, tente novamente.")

        while True:
            try:
                idade = int(input("Digite sua idade: "))

                if (idade >= 21):
                    break

                else:
                    print("Você não tem idade suficiente para alugar um carro: ")

            except ValueError:
                print("Idade inválida, tente novamente.")

        while True:
            email = input("Digite seu email: ")

            if("@" in email and ".com" in email):
                break

            else:
                print("Email inválido, tente novamente.")

        while True:
            cnh = input("Digite sua CNH: ")

            if(len(cnh) == 10 and cnh.isdigit()):
                break

            else:
                print("CNH inválida, tente novamente.")

        resp = input("Caso queira continuar cadastrando clientes, digite S: ").upper()

        match resp:
            case "S":
                print("Começando novo cadastro...")
            case _:
                break

    clie = Cliente(nome, cpf, telefone, idade, email, cnh)
    clientes.append(clie)

    print(clientes[0].get_cpf())

veiculos = []
clientes = []

while True:
    print("1 - CADASTRO DE VEÍCULOS\n2 - CADASTRO DE CLIENTES\n0 - ENCERRAR PROGRAMA")
    ope = input("Digite qual operação deseja fazer: ")

    match ope:
        case "1":
            cadastro_veiculos()

        case "2":
            cadastro_clientes()

        case "0":
            print("Encerrando programa...")
            break

        case _:
            print("Operação inválida, tente novamente.")






    




