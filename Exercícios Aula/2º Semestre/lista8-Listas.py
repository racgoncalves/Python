
#Exercício 01
'''
lista = []

i = 0

while i < 10:
    print("Digite a String",i+1,"de 10:")
    lista.append(input())

    i += 1

print(lista)
'''

#Exercício 02
'''
import random

n = int(input("Digite a quantidade de números que deseja: "))

lista = []

i = 0

while i < n:
    lista.append(random.randint(1,1001))
    i += 1

print(lista)
'''

#Exercício 03
'''
lista = []

i = 0

while i < 10:
    print("Digite a String",i+1,"de 10:")
    lista.append(input())

    i += 1

while i > 0:
    i -= 1
    print(lista[i])
'''

#Exercício 04
'''
n = int(input("Digite a quantidade de números que deseja: "))

lista = []

aux = 0

while aux < n:
    print("Digite o número real", aux + 1, "de",n,":")
    lista.append(float(input()))
    aux += 1

for i in range(0,len(lista)):
    if i >= aux: break
    print(lista[i]+lista[n-(i+1)])
    aux -= 1
'''

#Exercício 05
'''
def checaOrdenado(lista):
    n = 0
    while n < len(lista)-1:
        if lista[n] > lista[n+1]:
            return False
        n += 1
    return True

n = int(input("Digite a quantidade de números que deseja: "))

lista = []

aux = 0

while aux < n:
    print("Digite o número real", aux + 1, "de",n,":")
    lista.append(float(input()))
    aux += 1

print(checaOrdenado(lista))
'''

#Exercício 06
'''
def insereOrdenado(x, lista):

    for i in range (0 , len(lista)):
        if x < lista[i]:
            lista.insert(i,x)
            break
        if i == len(lista)-1:
            lista.insert(i+1,x)

        #Ou usando o append em vez do insert:
        #if i == len(lista)-1:
        #    lista.append(x)


vet = [1, 6, 10, 24, 25, 30, 45]
insereOrdenado(50, vet)
print(vet)
insereOrdenado(20, vet)
print(vet)
'''

#Exercício 07
'''
def contaMaior(lista, n):

    cont = 0
    for aux in lista:
        if aux >= n: cont += 1
    return cont

n = int(input("Digite a quantidade de números que deseja: "))

lista = []

aux = 0

while aux < n:
    print("Digite o número real", aux + 1, "de",n,":")
    lista.append(float(input()))
    aux += 1

num = float(input("Digite um número real: "))

print("\nA quantidade de números maiores ou iguais a",num,"na lista é:",contaMaior(lista,num))
'''

#Exercício 08
'''
def retornaPares(lista):

    listaNova = []
    for num in lista:
        if num%2 == 0: listaNova.append(num)
    return listaNova

n = int(input("Digite a quantidade de números que deseja: "))

lista = []

aux = 0

while aux < n:
    print("Digite o número inteiro", aux + 1, "de",n,":")
    lista.append(int(input()))
    aux += 1

print("Os números pares da lista são:",retornaPares(lista))
'''

#Exercício 09
'''
def retornaIguais(listaA,listaB):

    listaC = []
    for numA in listaA:
        for numB in listaB:
            if numA == numB: listaC.append(numA)
    return listaC

listaA = [2,5,8,99]

listaB = [1,3,8,99,125]

print(retornaIguais(listaA,listaB))
'''

#Exercício 10
'''
def intercala(listaA,listaB):

    listaC = []
    x = 0
    y = 0
    while x < len(listaA) or y < len(listaB):
        if y == len(listaB):
            listaC.append(listaA[x])
            x += 1
        elif x == len(listaA):
            listaC.append(listaB[y])
            y += 1
        elif listaA[x]<listaB[y]:
            listaC.append(listaA[x])
            x += 1
        elif listaB[y]<listaA[x]:
            listaC.append(listaB[y])
            y += 1
        else:
            listaC.append(listaA[x])
            #listaC.append(listaB[y])
            y += 1
            x += 1

    return listaC

listaA = [2,5,8,99]

listaB = [1,3,8,99,125]

print(intercala(listaA,listaB))
'''

#Exercício 11
'''
lista = ["Alemanha","Argentina","Bélgica","Brasil","Colômbia","Costa Rica","França","Holanda"]


for i in range(0,len(lista)):
    x = i + 1
    while x < len(lista):
        print("\nCampeão:",lista[i],"\nVice-Campeão:",lista[x])
        print("\nCampeão:",lista[x],"\nVice-Campeão:",lista[i])
        x += 1
'''

#Exercício 12
'''
lista = ['a','e','b','a','c','a','b','a','e']
listaB = []

for i in range(0,len(lista)):
    if not lista[i] in listaB:
        print(lista[i],":",lista.count(lista[i]))
        listaB.append(lista[i])
'''

#Exercício 13
'''
lista = [False] * 1000

for i in range(0,len(lista)):
    x = i
    while x < len(lista):
        if ((x+1) % (i+1)) == 0:
            if lista[i] == False:
                lista[i] = True
            else: lista[i] = False
        x += 1

for i in range(0,len(lista)):
    if lista[i] == True:
        print("\nA porta",i+1,"está aberta")
'''
