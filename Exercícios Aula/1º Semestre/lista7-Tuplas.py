
# ex 6
'''
import math

tupla = (5, 12, 26, 55, 234, 444, 592, 900)

soma = 0

for n in tupla:
    soma += n
media = soma/len(tupla)

x = 0
desvio = 0
for n in tupla:
    desvio += (n - media)**2

desvio = desvio/(len(tupla)-1)
desvio = math.sqrt(desvio)
print(desvio)
'''

# ex 7
'''
nomes = ("Ana", "Bia", "Celi", "Diana", "Eva", "Fabia")

parteNomes = nomes

tudo = ""

for n in nomes:
    x = 1
    while x < len(parteNomes):
        tudo += n + " e " + parteNomes[x] + ", "
        x += 1
    parteNomes = parteNomes[1:len(parteNomes)]

tudo = tudo[0:len(tudo)-2]

print(tudo)
'''

# ex 9
'''
inss = ((1317.07,0.08),(2195.12,0.09),(4390.24,0.11))

salario = float(input("Digite seu salário: "))

valor = 0.11 * 4390.24
for i in inss:
    if salario <= i[0]:
        valor = salario*i[1]
        break

print(round(valor,2))
'''