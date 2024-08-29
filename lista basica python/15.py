n = int(input("Digite até qual termo deseja ir: "))

fib = [1, 1]

for i in range(2, n+2):
    fibn = fib[i-1]+fib[i-2]
    fib.append(fibn)

print(*fib)
