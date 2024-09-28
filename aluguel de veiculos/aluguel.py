from classes import Aluguel
from main import clientes, veiculos

def aluguel():
    m31 = ["01", "03", "05", "07", "08", "10", "12"]
    m30 = ["04", "06", "09", "11"]
    print("=== ALUGUEL ===")

    while True:
        print("Escolha o cliente que irá alugar: ")
        for i in range(len(clientes)):
            print(f"{i} - NOME: {clientes[i].get_nome()} - CPF: {clientes[i].get_cpf()}")
        
        try:
            esc = int(input())
            if (esc in range(len(clientes))):
                cliente = clientes[esc]
                break
            else:
                print("Escolha inválida, tente novamente.")
        except ValueError:
            print("Escolha inválida, tente novamente.")

    while True:
        print("Escolha um veículo para alugar: ")
        for i in range(len(veiculos)):
            print(f"{i} - {veiculos[i].get_marca()} {veiculos[i].get_modelo()} - DIÁRIA -> R$ {veiculos[i].get_valor()} - {veiculos[i].get_status()}")
        
        try:
            esc = int(input())
            if (esc in range(len(veiculos)) and (veiculos[esc].get_status() == "Disponível")):
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

    while True:
        try:
            km_inicial = float(input("Digite a quilometragem inicial: "))
            if (km_inicial >= 0):
                break
            else:
                print("Quilometragem inválida, tente novamente.")

        except ValueError:
            print("Quilometragem inválida, tente novamente.")

    alug = Aluguel(cliente, veiculo, retirada, devolucao, km_inicial)
    return alug