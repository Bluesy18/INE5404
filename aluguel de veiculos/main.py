from classes import Veiculo, Cliente, Aluguel
import re

def cadastro_veiculos():

    cores = ["Branco", "Cinza", "Prata", "Preto", "Vermelho", "Azul"]
    marcas = ["Fiat", "Ford", "Volkswagen", "Chevrolet", "Peugeot", "Citroen"]
    fiatM = ["Strada", "Cronos", "Argo", "Mobi", "Uno"]
    fordM = ["Ka", "EcoSport"]
    volksM = ["Gol", "Polo", "Virtus", "Nivus", "Taos"]
    chevroM = ["Cobalt", "Onix", "Spin", "Cruze"]
    peugeotM = ["208", "2008"]
    citroenM = ["C3", "C4 Cactus"]

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

        resp = input("Caso queira continuar cadastrando veículos, digite S: ").upper()

        match resp:
            case "S":
                print("Começando novo cadastro...")
            case _:
                break

    veic = Veiculo(placa, cor, marca, modelo, ano)
    veiculos.append(veic)

    print(veiculos[0].get_modelo())

def cadastro_clientes():
    while True:
        print("=== CADASTRO DE CLIENTES ===")

        nome = input("Digite o nome: ")

        print(nome)

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
                idade = int(input("Digite a idade: "))

                if (idade >= 21):
                    break

                else:
                    print("Idade suficiente para alugar um carro: ")

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

        resp = input("Caso queira continuar cadastrando clientes, digite S: ").upper()

        match resp:
            case "S":
                print("Começando novo cadastro...")
            case _:
                break

    clie = Cliente(nome, cpf, telefone, idade, email, cnh)
    clientes.append(clie)

    print(clientes[0].get_cpf())



def aluguel():
    m31 = ["01", "03", "05", "07", "08", "10", "12"]
    m30 = ["04", "06", "09", "11"]
    print("=== ALUGUEL ===")
    while True:
        print("Escolha um veículo para alugar: ")
        for i in range(len(veiculos)):
            print(f"{i} - {veiculos[i].get_marca()} {veiculos[i].get_modelo()} - DIÁRIA -> R$ {veiculos[i].get_valor()}")
        
        try:
            esc = int(input())
            if (esc in range(len(veiculos))):
                veiculo = veiculos[esc]
                break
            else:
                print("Escolha inválida, tente novamente.")
        except ValueError:
            print("Escolha inválida, tente novamente.")

    while True:
        mesR = input("Digite o mês que acontecerá a retirada (usando dois digitos, ex: 01): ")

        if (mesR in m31) :
            while True:
                diaR = input("Digite o dia que acontecerá a retirada (usando dois digitos, ex: 01): ")
                if(len(diaR) == 2 and (1 <= int(diaR) <= 31)):
                    break
                else:
                    print("Dia inválido, tente novamente.")
            break

        elif (mesR in m30):
            while True:
                diaR = input("Digite o dia que acontecerá a retirada (usando dois digitos, ex: 01): ")
                if(len(diaR) == 2 and (1 <= int(diaR) <= 30)):
                    break
                else:
                    print("Dia inválido, tente novamente.")
            break

        elif (mesR == "02"):
            while True:
                diaR = input("Digite o dia que acontecerá a retirada (usando dois digitos, ex: 01): ")
                if(len(diaR) == 2 and (1 <= int(diaR) <= 28)):
                    break
                else:
                    print("Dia inválido, tente novamente.")
            break

        else:
            print("Mês inválido, tente novamente.")

    retirada = diaR+"/"+mesR

    while True:
        mesD = input("Digite o mês que acontecerá a devolução (usando dois digitos, ex: 01): ")

        if (mesD in m31) :
            while True:
                diaD = input("Digite o dia que acontecerá a devolução (usando dois digitos, ex: 01): ")
                if(len(diaD) == 2 and (1 <= int(diaD) <= 31)):
                    break
                else:
                    print("Dia inválido, tente novamente.")
            break

        elif (mesD in m30):
            while True:
                diaD = input("Digite o dia que acontecerá a devolução (usando dois digitos, ex: 01): ")
                if(len(diaD) == 2 and (1 <= int(diaD) <= 30)):
                    break
                else:
                    print("Dia inválido, tente novamente.")
            break

        elif (mesD == "02"):
            while True:
                diaD = input("Digite o dia que acontecerá a devolução (usando dois digitos, ex: 01): ")
                if(len(diaD) == 2 and (1 <= int(diaD) <= 28)):
                    break
                else:
                    print("Dia inválido, tente novamente.")
            break

        else:
            print("Mês inválido, tente novamente.")

    devolucao = diaD+"/"+mesD

    alug = Aluguel(veiculo, retirada, devolucao)
    alugueis.append(alug)

    alugueis[0].get_info()


veiculo_teste = Veiculo("ABC-1234", "Preto", "Volkswagen", "Virtus", 2022)
cliente_teste = Cliente("Davi", "13803015995", "48984480491", "21", "davirobergemachado@gmail.com", "1234567890")

alugueis = []
veiculos = [veiculo_teste]
clientes = [cliente_teste]

while True:
    print("1 - CADASTRO DE VEÍCULOS\n2 - CADASTRO DE CLIENTES\n3 - ALUGUEL\n0 - ENCERRAR PROGRAMA")
    ope = input("Digite qual operação deseja fazer: ")

    match ope:
        case "1":
            cadastro_veiculos()

        case "2":
            cadastro_clientes()

        case "3":
            aluguel()

        case "0":
            print("Encerrando programa...")
            break

        case _:
            print("Operação inválida, tente novamente.")






    




