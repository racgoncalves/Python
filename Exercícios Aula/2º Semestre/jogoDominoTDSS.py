import random

#retorno um conjunto de tamanho qtd
#contendo as pedras do domino
def distribui(pedras, qtd):
    retorno = []
    while qtd > 0:
        aux = pedras.pop(qtd)
        retorno.append(aux)
        qtd = qtd - 1
    
    return retorno

#retorna uma lista contendo 28 pedras que 
#representam o jogo de domino
def criaDomino():
    retorno = []
    j = 0
    while j <= 6:
        i = j
        while i <= 6:
            retorno.append([j, i])
            i = i + 1
        j = j + 1

    return retorno

def naoHaGanhador(listaA, listaB):
    if len(listaA) > 0 and len(listaB) > 0:
        return True
    else:
        return False

def mistura(lista):
    for x in range(1, 100):
        i = random.randint(0, len(lista)-1)
        j = random.randint(0, len(lista)-1)
        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp

def colocaPedra(p, pontas, mesa):
    if len(mesa) == 0:
        mesa.append(p)
        pontas.append(p[0])
        pontas.append(p[1])

    elif p[0] == pontas[0]:
        mesa.insert(0, p)
        pontas[0] = p[1]
    
    elif p[0] == pontas[1]:
        mesa.append(p)
        pontas[1] = p[1]
    
    elif p[1] == pontas[0]:
        mesa.insert(0, p)
        pontas[0] = p[0]
    
    elif p[1] == pontas[1]:
        mesa.append(p)
        pontas[1] = p[0]            

def jogadaCpu(mao, pontas, extras):
    i = 0
    while i < len(mao):
        peca = mao[i]
        if peca[0] in pontas or peca[1] in pontas:
            return mao.pop(i)
        i = i + 1
        if i == len(mao) and len(extras) > 0:
            mao.append(extras.pop())

    return [-1, -1]


def jogadaHomem(mao, pontas, extras):
    print(pontas)
    print(mao)
    pos = int(input("Digite pos da pedra ou -1 para comprar:"))
    while pos == -1 and len(extras)> 0:
        pedra_extra = extras.pop()
        mao.append(pedra_extra)
        print(mao)
        pos = int(input("Digite pos da pedra ou -1 para comprar:"))

    if pos != -1:
        return mao.pop(pos)
    else:
        return [-1, -1]    


domino = criaDomino()
mistura(domino)
maoHomem = distribui(domino, 7)
maoCpu = distribui(domino, 7)

mesa = []
extremos = []
vez = 1
while naoHaGanhador(maoHomem, maoCpu):
    if vez % 2 == 1:
        print(mesa)
        pedra = jogadaHomem(maoHomem, extremos, domino)
    else:    
        pedra = jogadaCpu(maoCpu, extremos, domino)
    colocaPedra(pedra, extremos, mesa)
    vez = vez + 1

if len(maoHomem) == 0:
    print("Parabéns, você ganhou da máquina")
else:
    print("Você conseguiu perder do computador")
 