def verifica0 (nome):
    while (len(nome) <= 3):
        nome = input("Digite seu nome novamente: ")
    return nome

def verifica1 (idade):
    while(not(0 <= idade <= 150)):
        idade = int(input("Digite sua idade novamente: "))
    return idade

def verifica2 (salario):
    while(salario < 0):
        salario = float(input("Digite seu salário novamente: "))
    return salario
    
def verifica3 (sexo):
    while((sexo != "f") and (sexo != "m")):
        sexo = input("Digite seu sexo novamente: ")
    return sexo

    
def verifica4 (estcivil, listestcivil):
    while (estcivil not in listestcivil):
        estcivil = input("Digite seu estado civil novamente: ")
    return estcivil

listestcivil = ['s', 'c', 'v', 'd']
    
nome = input("Digite seu nome: ")
nome = verifica0(nome)
idade = int(input("Digite sua idade: "))
idade = verifica1(idade)
salario = float(input("Digite seu salário: "))
salario = verifica2(salario)
sexo = input("Digite seu sexo: ")
sexo = verifica3(sexo)
estcivil = input("Digite seu estado civil: ")
estcivil = verifica4(estcivil, listestcivil)

print(nome, idade, salario, sexo, estcivil)



