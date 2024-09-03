n = int(input("Digite um número inteiro: "))

for _ in range (n, 1, -1):
    if (_ == n):
        fat = n*(_-1)
    else:
        fat = fat*(_-1)

print(fat)