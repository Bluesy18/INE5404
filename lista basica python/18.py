from random import randrange

lista = []

n = int(input("Digite quantos números terão: "))
m = int(input("Digite até que número será gerado: "))


for i in range(n):
    lista.append(randrange(0, m))

maior = max(lista)
menor = min(lista)
soma = sum(lista)

print(maior, menor, soma)