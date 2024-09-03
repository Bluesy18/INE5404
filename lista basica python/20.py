def verifica0(n):
    while (n >= 16):
        n = int(input("Número maior ou igual a 16! Digite novamente um número inteiro: "))

    return n

res = "S"

while (res == "S"):
    n = int(input("Digite um número inteiro: "))
    n = verifica0(n)

    for _ in range (n, 1, -1):
        if (_ == n):
            fat = n*(_-1)
        else:
            fat = fat*(_-1)

    print(fat)

    res = input("Deseja calcular novamente? (S/N): ").upper()