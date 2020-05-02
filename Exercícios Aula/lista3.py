#lista 3

#ex 1
'''
num = int(input("Digite um número inteiro: "))

if num > 10:
    print("Este número é maior do que 10")
'''

#ex 2
'''
num = int(input("Digite um número inteiro: "))

num2 = int(input("Digite outro número inteiro: "))

if (num > num2): print("Maior número:", num)
elif (num2 > num): print("Maior número:", num2)
else: print("Houve empate")
'''

#ex4
'''
time = input("Digite o nome do time da casa: ")
golstime = int(input("Digite quantos gols marcou: "))
time2 = input("Digite o nome do time visitante: ")
golstime2 = int(input("Digite quantos gols marcou: "))

if(golstime > golstime2): print("O vencedor foi",time)
elif(golstime < golstime2): print("O vencedor foi",time2)
else: print("Deu empate")
'''

#ex5
'''
diasUteis = int(input("Digite a quantidade de dias úteis do mês: "))
horasTrab = int(input("Digite a quantidade de horas trabalhadas: "))
salarioHr = float(input("Digite o valor do salário/hora: "))

jornadaNormal = diasUteis * 8
horaExtra = salarioHr * 1.5

if horasTrab > jornadaNormal:
    salarioNormal = jornadaNormal * salarioHr
    salarioExtra = (horasTrab - jornadaNormal) * horaExtra
    salarioFinal = salarioNormal + salarioExtra
    print("O trabalhador recebeu de hora extra o valor de: ",salarioExtra,
          " e o salário final foi de:",salarioFinal)
else:
    salarioNormal = horasTrab * salarioHr
    print("O salário final foi de:",salarioNormal)
'''

#ex6
'''
num = int(input("Digite um número inteiro: "))

num2 = int(input("Digite outro número inteiro: "))

if (num % num2 == 0): print("O número ",num," é divisível por ",num2)
else: print("O número ",num," não é divisível por ",num2)
'''

#ex7
'''
import math

num = float(input("Digite um número positivo: "))
while num < 1:
    num = float(input("Número inválido, digite um número positivo: "))

raiz = math.sqrt(num)

print("A raiz quadrada de ",num," é ",raiz)
'''

#ex8
'''
idade = int(input("Digite a idade do nadador: "))

if idade >= 5 and idade <= 7: categoria = "Infantil"
elif idade >= 8 and idade <= 10: categoria = "Juvenil"
elif idade >= 11 and idade <= 15: categoria = "Adolescente"
elif idade >= 16 and idade <= 30: categoria = "Adulto"
elif idade > 30: categoria = "Senior"
else: categoria = "Nenhuma"

print("Sua categoria é",categoria)
'''

#ex9
'''
num = int(input("Digite o número que será dividido: "))
num2 = int(input("Digite o número que irá pelo qual o anterior será dividido: "))

if num == 0 or num2 == 0: print("Impossível fazer uma divisão por 0")

else:
    divisao = num / num2
    print("O resultado da divisão é:",divisao)
'''

#ex10
'''
import math

a = int(input("Digite o coeficiente 'a' da equação: "))
b = int(input("Digite o coeficiente 'b' da equação: "))
c = int(input("Digite o coeficiente 'c' da equação: "))

delta = (b*b) - (4*a*c)
if delta < 0: print("A equação não possui raízes reais")

else:
    raiz = math.sqrt(delta)
    x1 = (-b + raiz)/(2*a)
    x2 = (-b - raiz)/(2*a)

    print("As raízes reais da equação são: x1 = ",round(x1,2)," e x2 = ",round(x2,2))
'''

#ex11
'''
preco = float(input("Digite o valor do produto: "))
escolha = 0

while escolha < 1 or escolha > 4:
    escolha = int(input("1 - A vista em dinheiro ou cheque, recebe 10% de desconto "
                        "\n2 - A vista no cartão de crédito, recebe 5% de desconto "
                        "\n3 - Em duas vezes, preço normal de etiqueta sem juros "
                        "\n4 - Em quatro vezes, preço normal de etiqueta mais juros de 7%"
                        "\nEscolha a sua opção de pagamento (1 a 4): "))

if escolha == 1:
    preco = preco - preco*0.1
    print("O valor total que irá pagar será de:",preco)

elif escolha == 2:
    preco = preco - preco*0.05
    print("O valor total que irá pagar será de:",preco)

elif escolha == 3:
    print("O valor total que irá pagar será de:",preco)

else:
    preco = preco + preco*0.07
    print("O valor total que irá pagar será de:",preco)
'''

#ex12
'''
media1 = float(input("Digite a média do primeiro semestre do aluno: "))
media2 = float(input("Digite a média do segundo semestre do aluno: "))
numAulas = int(input("Digite a quantidade de aulas ministradas: "))
numAssistiu = int(input("Digite a quantidad de aulas que o aluno assistiu: "))

mediaTotal = (media1 * 0.4) + (media2 * 0.6)
frequencia = (numAssistiu / numAulas) *100

if mediaTotal >= 6 and frequencia >= 70:
    print("A média do aluno foi",mediaTotal,"e sua frequencia foi de:",frequencia,
          "% portanto está aprovado")

elif mediaTotal < 6 and mediaTotal >=4 and frequencia >= 70:
    print("A média do aluno foi",mediaTotal,"e sua frequencia foi de:",frequencia,
          "% portanto está exame")

else: print("A média do aluno foi",mediaTotal,"e sua frequencia foi de:",frequencia,
          "% portanto está reprovado")
'''

#ex13
'''
listaMes = [31,28,31,30,31,30,31,31,30,31,30,31]

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))

mes -= 1

if mes > 11:
    print("Data inválida")

elif dia <= listaMes[mes]:
    print("Data válida")

else:
    print("Data inválida")
'''

#ex14
'''
listaMes = [31,28,31,30,31,30,31,31,30,31,30,31]

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if ano % 400 == 0:
    listaMes[1] = 29
elif ano % 100 != 0 and ano % 4 == 0:
    listaMes[1] = 29

mes -= 1

if mes > 11:
    print("Data inválida")

elif dia <= listaMes[mes]:
    print("Data válida")

else:
    print("Data inválida")
'''
