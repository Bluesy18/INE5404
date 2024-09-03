n = int(input("Digite um número inteiro: "))
p = True
divisores = []

while True:
    if (n == 1):
        print("Não é primo.")
        break

    for i in range(n-1, 1, -1):
        if (n%i == 0):
            divisores.append(i)
            p = False

    if (p == True):
        print("É primo.")
    else:
        print(f"{n} não é primo e é divisível por {divisores}")
    break


    
