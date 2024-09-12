from classes import Circulo
from subclasses import Quadrado, Retangulo

formas = []
ident = 0
res = "S"

while (res == "S"):

    op = input("Digite qual forma você deseja criar:\n1 - Retângulo\n2 - Quadrado\n3 - Círculo\n")
    
    while True:
        match op:
            case "1":
                b, h = map(float, input(f"Digite a base e a altura do retângulo {ident}: ").split())
                r = Retangulo(b, h, ident)
                r.calcula_area()
                r.calcula_perimetro()
                formas.append(r)
                r = None
                ident += 1
                break

            case "2":
                l = float(input(f"Digite o lado do quadrado {ident}: "))
                q = Quadrado(l, ident)
                q.calcula_area()
                q.calcula_perimetro()
                formas.append(q)
                q = None
                ident += 1
                break

            case "3":
                ra =float(input(f"Digite o raio do círculo {ident}: "))
                c = Circulo(ra, ident)
                c.calcula_area()
                c.calcula_perimetro()
                formas.append(c)
                c = None
                ident += 1
                break

            case _:
                print("Tente novamente.")

    res = input("Deseja cadastrar mais alguma forma? (S/N): ").upper()

for i in formas:
    print(f"{i.get_ident()}: ")
    print(f"Lados ou raio: {i.get_info()}")
    print(f"Perímetro: {i.get_perimetro()}")
    print(f"Área: {i.get_area()}")
           
    





