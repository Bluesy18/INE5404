from random import randrange

lista = []

n = int(input("Digite quantos números terão: "))

for i in range(n):
    lista.append(randrange(0, 1000))

maior = max(lista)
menor = min(lista)
soma = sum(lista)

print(maior, menor, soma)