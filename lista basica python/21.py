n = int(input("Digite um número inteiro: "))
p = True

while True:
    if (n == 1):
        print("Não é primo.")
        break

    for i in range(n-1, 1, -1):
        if (n%i == 0):
            print("Não é primo.")
            p = False
            break

    if (p == True):
        print("É primo.")
    break


    
