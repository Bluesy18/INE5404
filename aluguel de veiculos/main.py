from classes import Veiculo, Cliente, Aluguel, SistemaAluguel
from cadastro_veiculos import cadastro_veiculos
from cadastro_clientes import cadastro_clientes

def aluguel():
    m31 = ["01", "03", "05", "07", "08", "10", "12"]
    m30 = ["04", "06", "09", "11"]
    print("=== ALUGUEL ===")

    while True:
        print("Escolha o cliente que irá alugar: ")
        for i in range(len(sys.clientes)):
            print(f"{i} - NOME: {sys.clientes[i].get_nome()} - CPF: {sys.clientes[i].get_cpf()}")
        
        try:
            esc = int(input())
            if (esc in range(len(sys.clientes))):
                cliente = sys.clientes[esc]
                break
            else:
                print("Escolha inválida, tente novamente.")
        except ValueError:
            print("Escolha inválida, tente novamente.")

    while True:
        print("Escolha um veículo para alugar: ")
        for i in range(len(sys.veiculos)):
            print(f"{i} - {sys.veiculos[i].get_marca()} {sys.veiculos[i].get_modelo()} - DIÁRIA -> R$ {sys.veiculos[i].get_valor()} - {sys.veiculos[i].get_status()}")
        
        try:
            esc = int(input())
            if (esc in range(len(sys.veiculos)) and (sys.veiculos[esc].get_status() == "Disponível")):
                veiculo = sys.veiculos[esc]
                break
            elif(sys.veiculos[esc].get_status() == "Alugado"):
                print("Veículo alugado.")
                return None
            
            elif(sys.veiculos[esc].get_status() == "Em manutenção"):
                print("Veículo em manutenção.")
                return None
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
        if (len(sys.alugueis) == 0):
            print("Não existem alugueis ativos.")

        else:
            print("Selecione em qual aluguel deseja efetuar a devolução: ")
            for k in range(len(sys.alugueis)):
                print(f"{k} - {sys.alugueis[k].cliente.get_nome()} - {sys.alugueis[k].veiculo.get_modelo()}")
            try:
                esco = int(input())
                if (esco in range(len(sys.alugueis))):
                    while True:
                        km_rodada = float(input("Digite a quilometragem que foi rodada: "))
                        if(km_rodada >= 0):
                            km_final = sys.alugueis[esco].get_km_inicial() + km_rodada
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
                                sys.alugueis[esco].veiculo.set_manutencao()
                                sys.alugueis.pop(esco)
                                for _ in sys.alugueis:
                                    print(_)
                                break

                            case "N":
                                multa_dano = 0
                                sys.alugueis[esco].veiculo.set_disponivel()
                                sys.alugueis.pop(esco)
                                for _ in sys.alugueis:
                                    print(_)
                                break

                            case _:
                                print("Resposta inválida, tente novamente.")

                    multa = multa_dano + (atraso*200)

                    if (multa > 0):
                        sys.set_receita(multa)
                        print(f"O veículo está com uma quilometragem final de {km_final} km e houve ma multa de R$ {multa}")

                    else:
                        print(f"O veículo está com uma quilometragem final de {km_final} km")

                else:
                    print("Escolha inválida, tente novamente.")

            except ValueError:
                print("Escolha inválida, tente novamente.")

def frota():
    print("Selecione um veículo: ")
    for i in range(len(sys.veiculos)):
            print(f"{i} - {sys.veiculos[i].get_marca()} {sys.veiculos[i].get_modelo()} - {sys.veiculos[i].get_placa()}")
    while True:
        try:
                esc = int(input())
                if (esc in range(len(sys.veiculos))):
                    veiculo = sys.veiculos[esc]
                    break
                else:
                    print("Escolha inválida, tente novamente.")
        except ValueError:
            print("Escolha inválida, tente novamente.")
    
    print("\n1 - CONSULTAR INFORMAÇÕES\n2 - MANDAR/TIRAR DA MANUTENÇÃO\n")
    opera = input()
    while True:
        match opera:
            case "1":
                print(veiculo)
                break

            case "2":
                if(veiculo.get_status() == "Disponível"):
                    veiculo.set_manutencao()
                    
                elif(veiculo.get_status() == "Em manutenção"):
                    veiculo.set_disponivel()
                
                else:
                    print("O veículo está alugado e não pode ser mandado para manutenção.")
                    
                break

            case _:
                print("Operação inválida, tente novamente.")

def con_clientes():
    while True:
        print("Selecione um cliente: ")
        for i in range(len(sys.clientes)):
            print(f"{i} - NOME: {sys.clientes[i].get_nome()} - CPF: {sys.clientes[i].get_cpf()}")
        
        try:
            esc = int(input())
            if (esc in range(len(sys.clientes))):
                cliente = sys.clientes[esc]
                break
            else:
                print("Escolha inválida, tente novamente.")
        except ValueError:
            print("Escolha inválida, tente novamente.")

    print(cliente)

def pagar():
    while True:
        if(len(sys.alugueis) == 0):
            print("Não existem alugueis ativos.")
            break
        else:
            print("Selecione qual aluguel deseja pagar: ")
            for j in range(len(sys.alugueis)):
                print(f"{j} - {sys.alugueis[j].cliente.get_nome()} - {sys.alugueis[j].veiculo.get_modelo()}")
            try:
                esco = int(input())
                if (esco in range(len(sys.alugueis)) and (sys.alugueis[esco].get_pagamento() == "Pendente")):
                    sys.alugueis[esco].veiculo.set_alugado()
                    sys.alugueis[esco].set_pagamento()
                    sys.alugueis[esco].cliente.set_historico(sys.alugueis[esco].veiculo.get_modelo(), sys.alugueis[esco].get_retirada(), sys.alugueis[esco].get_devolucao())
                    print(sys.alugueis[esco])
                    sys.set_receita(sys.alugueis[esco].get_valor_total())
                    break
                elif (sys.alugueis[esco].get_pagamento() == "Pago"):
                    print("Aluguel já foi pago.")
                    break
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

sys = SistemaAluguel(clientes, veiculos, alugueis)

while True:
    print("\n1 - CADASTRO DE VEÍCULOS\n2 - CADASTRO DE CLIENTES\n3 - ALUGUEL\n4 - DEVOLUÇÃO\n5 - CONSULTAR FROTA\n6 - CONSULTAR CLIENTES\n7 - RELATÓRIO DE RECEITA\n0 - ENCERRAR PROGRAMA\n")
    ope = input("Digite qual operação deseja fazer: ")

    match ope:
        case "1":
            sys.veiculos.append(cadastro_veiculos())

        case "2":
            sys.clientes.append(cadastro_clientes())

        case "3":
            print("1 - NOVO ALUGUEL\n2 - PAGAR ALUGUEL")
            op2 = input("Digite qual operação deseja fazer: ")

            match op2:
                case "1":
                    sys.alugueis.append(aluguel())

                case "2":
                    while True:
                        if(len(sys.alugueis) == 0):
                            print("Não existem alugueis ativos.")
                        else:
                            pagar()
                        break
                case _:
                    print("Operação inválida, tente novamente.")

        case "4":
            devolucao()

        case "5":
            frota()

        case "6":
            con_clientes()

        case "7":
            print(f"R$ {sys.get_receita()}")

        case "0":
            print("Encerrando programa...")
            break

        case _:
            print("Operação inválida, tente novamente.")






    




