a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))


if (a < b):
    lista = list(range(a, b, 1))
    for i in lista:
        print(i)

elif (b < a):
    lista = list(range(b, a, 1))
    for i in lista:
        print(i)

else:
    print("Não existem inteiros nesse intervalo")
