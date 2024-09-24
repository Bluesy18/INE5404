from classes import Veiculo
import re

placa_padrao = r'^[A-Z]{3}-\d{4}$'

veiculos = []

cores = ["Branco", "Cinza", "Prata", "Preto", "Vermelho", "Azul"]
marcas = ["Fiat", "Ford", "Volkswagen", "Audi", "Chevrolet", "Peugeot", "Citroen"]
fiatM = ["Strada", "Cronos", "Argo", "Mobi", "Uno", "Toro"]
fordM = ["Ka", "EcoSport"]
volksM = ["Gol", "Polo", "Virtus", "Nivus", "Taos"]
chevroM = ["Cobalt", "Onix", "Spin", "Cruze"]
peugeotM = ["208", "2008"]
citroenM = ["C3", "C4 Cactus", "Aircross"]
audiM = ["A3", "A4", "A5"]

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

    # marcas = ["Fiat", "Ford", "Volkswagen", "Audi", "Chevrolet", "Peugeot", "Citroen"]


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
    resp = input("Digite S para continuar: ").upper()

    match resp:
        case "S":
            print("Começando novo cadastro...")
        case _:
            break

veic = Veiculo(placa, cor, marca, modelo, ano, status)
veiculos.append(veic)

print(veiculos[0].get_modelo())
