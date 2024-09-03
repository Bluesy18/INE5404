n = int(input("Digite um número inteiro: "))
primos = []
cont = 0

for i in range(2, n+1):
    p = True
    for j in range((int(i**0.5)), 1, -1):
        cont += j
        if(i%j == 0):
            p = False
    if (p == True):
        primos.append(i)

print(f"Os primos são {primos} e a quantidade total de divisões foi de {cont}.")



        



    

