b = float(input("Digite a base: "))
e = int(input("Digite o expoente: "))

for i in range(e-1):
    if (i == 0):
        n = b
    n = n*b

print(n)