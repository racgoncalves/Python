
# Rodrigo André Chiarelli Gonçalves RM: 85716

#exercício 1
'''
salario = 500
comissao = 0
num = 0

funcionario = input("\nLançamento de Comissão da loja MaxRoupas\n"
                    "Digite o nome do funcionário: ")

while (num != 5):

    num = int(input("\n1 - camisetas e polos\n"
                    "2 - calças e camisas\n"
                    "3 - jaquetas e agasalhos\n"
                    "4 - ternos e sobretudos\n"
                    "5 - Mostrar o salário total e finalizar o programa\n"
                    "Digite a categoria do produto que deseja inserir o valor de vendas: "))

    if (num == 1):
        comissao = float(input("Digite o valor vendido de camisetas e polos: "))
        comissao *= 0.04
        salario += comissao

    if (num == 2):
        comissao = float(input("Digite o valor vendido de calças e camisas: "))
        comissao *= 0.055
        salario += comissao

    if (num == 3):
        comissao = float(input("Digite o valor vendido de jaquetas e agasalhos: "))
        comissao *= 0.07
        salario += comissao

    if (num == 4):
        comissao = float(input("Digite o valor vendido de ternos e sobretudos: "))
        comissao *= 0.085
        salario += comissao

    if (num == 5): print("\nO salário total de",funcionario,"foi de: R$",round(salario,2))
'''

#exercício 2
'''
aulasSemanais = int(input("Digite o número de aulas semanais do professor: "))

horaAula = float(input("Digite o valor da hora/aula do professor: "))

salBase = aulasSemanais*4.5*horaAula
descanso = salBase/6
horaAtividade = 0.05*(salBase + descanso)

print ("Salário base: R$",round(salBase,2))
print ("DSR: R$",round(descanso,2))
print ("Hora Atividade: R$",round(horaAtividade,2))
print ("Salário Mensal: R$",round(salBase+descanso+horaAtividade,2))
'''

#exercício 3
'''
a = 0
b = 0
i = 2
mmc = 1

print ("\nCálculo de Mínimo Múltiplo Comum (MMC)\n")

while (a <= 0):
    a = int(input("Digite um número inteiro e positivo: "))

divA = a

while (b <= 0):
    b = int(input("Digite outro número inteiro e positivo: "))

divB = b

while (divA > 1 or divB > 1):

    while (divA % i == 0 or divB % i == 0):

        if (divA % i == 0 and divB % i == 0):
            divA /= i
            divB /= i
            mmc *= i

        elif (divA % i == 0):
            divA /= i
            mmc *= i

        elif (divB % i == 0):
            divB /= i
            mmc *= i
    i += 1

print ("\nO MMC de",a,"e",b,"é",mmc)
'''

#exercício 4
'''
a = 0
b = 0
mdc = 0

print ("\nCálculo de Máximo Divisor Comum (MDC)\n")

while (a <= 0):
    a = int(input("Digite um número inteiro e positivo: "))

while (b <= 0):
    b = int(input("Digite outro número inteiro e positivo: "))

i = min(a,b)

while (i > 0):
    if(a%i == 0 and b%i == 0):
        mdc = i
        break
    else:
        i -= 1

print ("O MDC de",a,"e",b,"é",mdc)
'''