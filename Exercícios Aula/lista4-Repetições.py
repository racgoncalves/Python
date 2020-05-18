#lista 4

#ex 1
'''
#recebendo o número

numero = int(input("Digite um número inteiro negativo: "))

resultado = 0

while numero < 0:
    if numero % 2 == 0:
        resultado += numero
    numero += 1

print("O resultado é:",resultado)
'''

'''
#recebendo uma lista pronta

lista = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0]

soma = 0

for num in lista:
    if num % 2 == 0:
        soma += num

print("A soma dos números da lista é:",soma)
'''

#ex 2
'''
numAlunos = int(input("Digite a quantidade de alunos da turma: "))

i = 1

dicionario = {}

while i <= numAlunos:
    print("Digite a nota do aluno", i, ":")
    dicionario[i] = [float(input())]
    i += 1

totalNotas = 0

for objeto in dicionario.values():
    totalNotas += objeto[0]

media = totalNotas / numAlunos

print(dicionario)
print("A média dos alunos desta turma foi de:",round(media,2))
'''

#ex 3
'''
numAlunos = int(input("Digite a quantidade de alunos da turma: "))

i = 1

contReprovado = 0
contAprovado = 0

dicionario = {}

while i <= numAlunos:
    print("Digite a nota do aluno", i, ":")
    notaAluno = float(input())
    dicionario[i] = [notaAluno]
    i += 1
    if notaAluno >= 0 and notaAluno < 5:
        contReprovado += 1
    else: contAprovado +=1

totalNotas = 0

for objeto in dicionario.values():
    totalNotas += objeto[0]

media = totalNotas / numAlunos

print(dicionario)
print("A média dos alunos desta turma foi de:",round(media,2))
print("A quantidade de reprovados foi de:",contReprovado)
print("A quantidade de aprovados foi de:",contAprovado)
'''

#ex 4
'''
numero = int(input("Digite a quantidade números que deseja digitar: "))

i = 0

negativo = 0

positivo = 0

while i < numero:
    real = float(input("Digite um número real: "))
    i += 1
    if real > 0: positivo += 1
    if real < 0: negativo += 1

print("A quantidade de números positivos foi de:",positivo)
print("A quantidade de números negatiavos foi de:",negativo)
'''

#ex 5
'''
lista = []

numero = int(input("Digite um número inteiro positivo: "))

divisor = 1

while divisor <= numero:
    if numero % divisor == 0:
        lista.append(divisor)
    divisor += 1

print("Os divisores positivos de",numero,"são",lista)
'''

#ex 6
'''
i = 1

maiorNota = 0
menorNota = 70

ate20 = 0
mais20 = 0
mais50 = 0


while i <= 20:
    nota = -1
    while nota < 0 or nota > 70:
        print("Digite a pontuação do candidato",i,":")
        nota = int(input())
    i += 1
    if nota > maiorNota: maiorNota = nota
    if nota < menorNota: menorNota = nota
    if nota <= 20: ate20 += 1
    if nota > 20 and nota <= 50: mais20 += 1
    if nota > 50: mais50 += 1

print("A maior nota foi:",maiorNota)
print("A menor nota foi:",menorNota)
print("A quantidade de pessoas que fizeram até 20 pontos:",ate20)
print("A quantidade de pessoas que fizeram mais de 20 pontos e menos de 50:",mais20)
print("A quantidade de pessoas que fizeram mais de 50 pontos:",mais50)
'''

#ex 7
'''
f = 50

while f <= 150:
    c = ((f - 32) * 5) / 9
    print("Para",f,"graus Fahrenheit teremos",round(c,1),"graus centígrados")
    f += 1
'''

#ex 8
'''
#usando while

numero = int(input("Digite um número inteiro positivo: "))

i = 2
aux = 0

while i < numero:
    if numero % i == 0:
        print("O número não é primo")
        aux = 2
        break
    i += 1

if aux == 0:
    print("O número é primo")
'''

'''
#usando for

n = int(input("Verificar numeros primos ate: "))
mult=0

for count in range(2,n):
    if (n % count == 0):
        print("Múltiplo de",count)
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("Tem",mult," múltiplos acima de 2 e abaixo de",n)
'''

#ex 9
'''
d = float(input("Digite o dinheiro a ser aplicado: "))
j = float(input("Digite a taxa de juros da aplicação em %: ")) / 100
t = int(input("Digite a quantidade de meses da aplicação: "))

for mes in range(0,t):
    d += d*j

print("O total ao final da aplicação foi de",round(d,2),"reais")
'''

#ex 10
'''
n = int(input("Digite um número inteiro positivo: "))

i = 1
fatorial = 1

while i <= n:
    fatorial *= i
    i += 1

print(n,"fatorial é igual a",fatorial)
'''

#ex 11
'''
#usando while

numero = int(input("Digite um número inteiro positivo: "))

i = 2
aux = 0

while i < numero:
    if numero % i == 0:
        print("O número não é primo")
        aux = 2
        break
    i += 1

if aux == 0:
    print("O número é primo")
'''

'''
#usando for

n = int(input("Verificar numeros primos ate: "))
mult=0

for count in range(2,n):
    if (n % count == 0):
        print("Múltiplo de",count)
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("Tem",mult," múltiplos acima de 2 e abaixo de",n)
'''

#ex 12
'''
n = int(input("Digite o número da sequência de Fibonacci que deseja saber: "))

fAnterior = 1
f = 1

i = 2

while i < n:
    fAnterior2 = fAnterior
    fAnterior = f
    f = fAnterior + fAnterior2
    i += 1

print("O número",n,"da sequência de Fibonacci é:",f)
'''

#ex 13
'''
num = int(input("Digite um número inteiro positivo:"))

x = 1
lista = []

while x < num:
    u = int((num // x) % 10)
    x *= 10
    lista.append(u)

print(lista)

n = 0

ultimo = len(lista)-1
penultimo = len(lista)-2

if lista[0] == lista[ultimo] and lista[1] == lista[penultimo]:

    print("O número",num,"é palíndromo")
else:
    print("O número",num,"não é palíndromo")
'''

#ex 14
'''
num = int(input("Digite um número inteiro positivo:"))

x = 1
lista = []

while x < num:
    u = int((num // x) % 10)
    x *= 10
    lista.append(u)

print(lista)

n = 0

while n < len(lista):

    mult2 = lista[n] * 2

    if mult2 >= 10:
        n1 = (mult2 % 10)
        n2 = (mult2 // 10) % 10
        mult2 = n1 + n2

    lista[n] = mult2

    n += 2

parteCod = int(sum(lista) % 10)

if parteCod == 0:
    cod = 0
else:
    cod = 10 - parteCod

print(lista)

print("O dígito de controle do número",num,"é",cod)
'''
