fib = [0, 1, 1]
fibn = 0

while (fibn <= 500):
    fibn = fib[-1]+fib[-2]
    fib.append(fibn)

print(*fib)
