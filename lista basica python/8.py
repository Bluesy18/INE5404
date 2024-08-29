soma = 0

numeros = []
for i in range (5):
    n = float(input("Digite um número: "))
    numeros.append(n)

for _ in numeros:
    soma += _

media = soma/len(numeros)

print(f"A soma é de {soma} e a média é {media}")
