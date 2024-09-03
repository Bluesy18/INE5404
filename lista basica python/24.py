from random import randint

n = int(input("Digite a quantidade de notas: "))
notas = []

for i in range(n):
    notas.append(randint(0, 10))

media = sum(notas)/len(notas)
print(notas)
print(media)
