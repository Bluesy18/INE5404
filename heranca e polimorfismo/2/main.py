from subclasses import Normal
from camarotes import CamaroteInferior, CamaroteSuperior

while True:
    resp = input("Qual ingresso você vai querer? (N)ormal ou (V)IP: ").upper()

    match resp:
        case "N":
            i = Normal()
            break
        case "V":
            while True:
                rvip = input("Camarote inferior ou superior? (S)uperior/(I)nferior: ").upper()
                match rvip:
                    case "S":
                        i = CamaroteSuperior()
                        break
                    case "I":
                        i = CamaroteInferior()
                        break
                    case _:
                        print("Tente novamente.")
            break
        case _:
            print("Tente novamente.")

i.imprimeValor()

if(i.get_valor() == 10.0):
    i.normal()

if(i.get_valor() == 20.0):
    print(i.get_local())

