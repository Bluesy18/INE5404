from assistentes import Tec, Admin

def verifica0(turno):
    while ((turno != "M") and (turno != "N")):
        turno = input("Digite novamente o seu turno (M(atutino) ou N(oturno): ").upper()
    return turno

matricula = int(input("Digite a matrícula do funcionário: "))
salario = float(input("Digite o salário do funcionário: "))
turno = input("Digite o seu turno (M(atutino) ou N(oturno): ").upper()
turno = verifica0(turno)
t = Tec(matricula, salario)
a = Admin(matricula, salario, turno)
print(t.get_matricula())
print(t.get_salario())
print(a.get_matricula())
print(a.get_salario())  
print(a.get_turno()) 