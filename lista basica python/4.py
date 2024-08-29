def crescA(a):
    a = a+(a*0.03)
    return a

def crescB(b):
    b = b+(b*0.015)
    return b

a = 80000
b = 200000
anos = 0

while (a < b):
    a = crescA(a)
    b = crescB(b)
    anos += 1

print(f"A quantidade de anos para a população A ultrapassar ou igualar a B é de {anos}")

