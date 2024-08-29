a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))

soma = 0

if (a < b):
    lista = list(range(a, b, 1))
    for i in lista:
        soma += i
        print(i)
    print(f"Soma: {soma}")

elif (b < a):
    lista = list(range(b, a, 1))
    for i in lista:
        soma += i
        print(i)
    print(f"Soma: {soma}")

else:
    print("Não existem inteiros nesse intervalo")
