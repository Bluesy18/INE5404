lista = []
pares = 0
impares = 0

for _ in range(10):
    n = int(input("Digite um número inteiro: "))
    lista.append(n)

for num in lista:
    if(num%2 == 0):
        pares += 1
    else:
        impares += 1

print(f"Quantidade de pares: {pares}\nQuantidade de ímpares: {impares}")