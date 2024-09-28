from classes import Veiculo, Cliente, Aluguel
from cadastro_veiculuos import cadastro_veiculos
from cadastro_clientes import cadastro_clientes
import re

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

def devolucao():
        print("Selecione em qual aluguel deseja efetuar a devolução: ")
        for k in range(len(alugueis)):
            print(f"{k} - {alugueis[k].cliente.get_nome()} - {alugueis[k].veiculo.get_modelo()}")
            try:
                esco = int(input())
                if (esco in range(len(alugueis))):
                    while True:
                        km_rodada = float(input("Digite a quilometragem que foi rodada: "))
                        if(km_rodada >= 0):
                            km_final = alugueis[esco].get_km_inicial() + km_rodada
                            break
                        else:
                            print("Quilometragem inválida, tente novamente.")
                    
                    while True:
                        atraso = int(input("Houve atraso de quantos dias? (Caso não haja atraso, digite 0): "))
                        if (atraso >= 0):
                            break
                        else:
                            print("Atraso inválido, tente novamente.")

                    while True:
                        dano = input("Houve danos ao veículo? (S/N): ").upper()
                        match dano:
                            case "S":
                                multa_dano = 1000
                                alugueis[esco].veiculo.set_manutencao()
                                alugueis.pop(esco)
                                break

                            case "N":
                                multa_dano = 0
                                alugueis[esco].veiculo.set_disponivel()
                                alugueis.pop(esco)
                                break

                            case _:
                                print("Resposta inválida, tente novamente.")

                    multa = multa_dano + (atraso*50)

                    if (multa > 0):
                        print(f"O veículo está com uma quilometragem final de {km_final} km e houve ma multa de R$ {multa}")

                    else:
                        print(f"O veículo stá com uma quilometragem final de {km_final} km")


                else:
                    print("Escolha inválida, tente novamente.")

            except ValueError:
                print("Escolha inválida, tente novamente.")

    

veiculo_teste = Veiculo("ABC-1234", "Preto", "Volkswagen", "Virtus", 2022)
cliente_teste = Cliente("Davi", "13803015995", "48984480491", "21", "davirobergemachado@gmail.com", "1234567890")
aluguel_teste = Aluguel(cliente_teste, veiculo_teste, "02/02", "04/02", 1000)

alugueis = [aluguel_teste]
veiculos = [veiculo_teste]
clientes = [cliente_teste]

while True:
    print("1 - CADASTRO DE VEÍCULOS\n2 - CADASTRO DE CLIENTES\n3 - ALUGUEL\n4 - DEVOLUÇÃO\n0 - ENCERRAR PROGRAMA")
    ope = input("Digite qual operação deseja fazer: ")

    match ope:
        case "1":
            veiculos.append(cadastro_veiculos())

        case "2":
            clientes.append(cadastro_clientes())

        case "3":
            print("1 - NOVO ALUGUEL\n2 - PAGAR ALUGUEL")
            op2 = input("Digite qual operação deseja fazer: ")

            match op2:
                case "1":
                    alugueis.append(aluguel())

                case "2":
                    while True:
                        print("Selecione qual aluguel deseja pagar: ")
                        for j in range(len(alugueis)):
                            print(f"{j} - {alugueis[j].cliente.get_nome()} - {alugueis[j].veiculo.get_modelo()}")
                        try:
                            esco = int(input())
                            if (esco in range(len(alugueis))):
                                alugueis[esco].veiculo.set_alugado()
                                alugueis[esco].set_pagamento()
                                alugueis[esco].cliente.set_historico(alugueis[esco].veiculo.get_modelo(), alugueis[esco].get_retirada(), alugueis[esco].get_devolucao())
                                alugueis[esco].get_info()
                                break
                            else:
                                print("Escolha inválida, tente novamente.")
                        except ValueError:
                            print("Escolha inválida, tente novamente.")
                case _:
                    print("Operação inválida, tente novamente.")

        case "4":
            devolucao()


        case "0":
            print("Encerrando programa...")
            break

        case _:
            print("Operação inválida, tente novamente.")






    




