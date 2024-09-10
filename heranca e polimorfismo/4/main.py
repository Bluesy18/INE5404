from camarotes import CamaroteInferior, CamaroteSuperior
from assistentes import Tec, Admin
from subclasses import Normal, Novo, Velho

adm = Admin()
tec = Tec()

print(f"Assistente administrativo: {adm.get_nome()}, Matrícula: {adm.get_matricula()}")
print(f"Assistente técnico: {tec.get_nome()}, Matrícula: {tec.get_matricula()}")

while True:

    op = input("Digite 1 para o ingresso normal e 2 para o VIP: ")

    match op:
        case "1":
            ing = Normal()
            print("Ingresso normal.")
            break
        case "2":
            print("Ingresso VIP.")
            while True:
                cam = input("Digite 1 para camarote superior e 2 para camarote inferior: ")
                match cam:
                    case "1":
                        ing = CamaroteSuperior()
                        print("Camarote superior.")
                        break
                    case "2":
                        ing = CamaroteInferior()
                        print("Camarote inferior.")
                        break
                    case _:
                        print("Tente novamente.")
            break
        case _:
            print("Tente novamente.")
print(f"Valor do ingresso: R$ {ing.get_valor()}")

while True:
    ops = input("Digite 1 para um imóvel novo e 2 para um imóvel velho: ")
    match ops:
        case "1":
            im = Novo()
            break
        case "2":
            im = Velho()
            break
        case _:
            print("Tente novamente.")
print(f"Imóvel em {im.get_endereco()}, custando R$ {im.get_valor()}")



