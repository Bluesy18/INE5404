def crescA(a, taxA):
    a = a+(a*taxA)
    return a

def crescB(b, taxB):
    b = b+(b*taxB)
    return b

def verifica0(a, b):
    while (a >= b):
        a = int(input("A população A é maior ou igual do que a B, então digite novamente: "))
    return a

res = "S"

while(res == "S"):

    b = int(input("Digite a população de B: "))
    taxB = float(input("Digite a taxa de crescimento de B: "))
    taxB = taxB/100
    a = int(input("Digite a população de A: "))
    a = verifica0(a, b)
    taxA = float(input("Digite a taxa de crescimento de A: "))
    taxA = taxA/100

    anos = 0

    try: 
        while (a < b):
            a = crescA(a, taxA)
            b = crescB(b, taxB)
            anos += 1
        print(f"A quantidade de anos para a população A ultrapassar ou igualar a B é de {anos} anos.")

    except:
        print("Nunca ultrapassará.")

    res = input("Deseja continuar? (S/N): ").upper()


