
#Exercício 01
def retornaNumeros(x):
    lista = []
    i = 1
    while i < x:
        lista.append(i)
        i += 1
    return lista

#Exercício 02
def mistura(listaA):
    import random

    listaB = []
    i = 0

    while i < len(listaA):
        num = listaA[random.randrange(len(listaA))]
        while num in listaB:
            num = listaA[random.randrange(len(listaA))]
        listaB.append(num)
        i += 1
    return listaB

#Exercício 03
def descartar(lista):
    print(lista)
    elemento = int(input("\nEscolha um elemento para ser descartado: "))
    while elemento not in lista:
        print(lista)
        elemento = int(input("\nEscolha um elemento para ser descartado: "))
    for i in range(0,len(lista)):
        if lista[i] == elemento:
            lista.pop(i)
            print("\nElemento",elemento,"foi descartado!\n")
            return elemento

#Exercício 04
def compara(x, y):
    if x > y: return -1
    elif x == y: return 0
    else: return 1

#Truco

lista = mistura(retornaNumeros(28))

mao1 = lista[0:3]
mao2 = lista[3:6]


resultado = 0

while resultado > -2 and resultado < 2 and len(mao1) > 0:
    jogador1 = descartar(mao1)
    jogador2 = descartar(mao2)
    resultado += compara(jogador1,jogador2)
    print(resultado,'\n')

if resultado > 0: print("Jogador 2 ganhou")
else: print("jogador 1 ganhou")
