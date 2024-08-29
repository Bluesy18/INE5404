def verifica0(n):
    while (n < 0 or n > 10):
        n = float(input("Erro! Digite novamente uma nota entre 0 e 10: "))
    return n

n = float(input("Digite uma nota entre 0 e 10: "))
n = verifica0(n)

