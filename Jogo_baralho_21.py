# Jogos de Barallho

import random

def mudaNome(carta):
    if carta[0] == 1:
        carta = "A",carta[1]
    elif carta[0] == 11:
        carta = "J",carta[1]
    elif carta[0] == 12:
        carta = "Q",carta[1]
    elif carta[0] == 13:
        carta = "K",carta[1]
    return carta

def validaCarta(carta,cartas):
    for c in cartas:
        if c == carta:
            return False
    return True

def validaCartaCPU(carta,cartas,cartasCPU):
    for c in cartas:
        if c == carta:
            return False
    for c in cartasCPU:
        if c == carta:
            return False
    return True

def baralho21(carta,cartas,pontuacao):
    if carta[0] == 11 or carta[0] == 12 or carta[0] == 13:
        carta = 10,carta[1]
    elif carta[0] == 1 and pontuacao < 11:
        print("\nCartas:",cartas)
        a = 0
        while a != 1 and a != 11:
            try:
                a = int(input("Digite o valor do Ás (1 ou 11): "))
            except:
                print("\nDigite apenas números!\n")
                a = 0
        carta = a,carta[1]
    return carta

def baralho21CPU(carta,pontuacao):
    if carta[0] == 11 or carta[0] == 12 or carta[0] == 13:
        carta = 10,carta[1]
    elif carta[0] == 1 and pontuacao < 11:
        carta = 11,carta[1]
    return carta

def maiorCarta(valores, naipes):

    # Sua Carta
    cartaVoce = (valores[random.randrange(len(valores))],naipes[random.randrange(len(naipes))])

    # Carta da CPU
    cartaCPU = cartaVoce
    while cartaCPU == cartaVoce:
        cartaCPU = (valores[random.randrange(len(valores))],naipes[random.randrange(len(naipes))])

    # Resultados
    ganhador = "empate"

    if cartaVoce[0] > cartaCPU[0]:
        ganhador = "Você"
    if cartaVoce[0] < cartaCPU[0]:
        ganhador = "CPU"

    print("\nVocê:",mudaNome(cartaVoce),"\nCPU:",mudaNome(cartaCPU),"\nGanhador:",ganhador)

def blackjack(valores, naipes):

    #Você
    pontuacao = 0
    resposta = "s"

    # Sorteando suas 2 primeiras cartas
    carta1 = (valores[random.randrange(len(valores))],naipes[random.randrange(len(naipes))])

    carta2 = carta1
    while carta2 == carta1:
        carta2 = (valores[random.randrange(len(valores))],naipes[random.randrange(len(naipes))])

    # Junta as cartas
    cartas = [mudaNome(carta1),mudaNome(carta2)]

    # Gera pontuação
    pontuacao = baralho21(carta1,cartas,pontuacao)[0]
    pontuacao += baralho21(carta2,cartas,pontuacao)[0]

    # Adicionando mais cartas
    while resposta == "s" and pontuacao < 21:
        resposta = ""
        print("\nCartas:",cartas,"\nTotal de pontos:",pontuacao)

        # Pergunta se quer mais cartas
        while resposta != "s" and resposta != "n":
            resposta = input("\nVocê deseja uma nova carta (digite 'S' para SIM ou 'N' para NÃO): ").lower()
        if resposta == "s":
            cartaNova = (valores[random.randrange(len(valores))], naipes[random.randrange(len(naipes))])

            # Valida a carta
            while not validaCarta(cartaNova,cartas):
                cartaNova = (valores[random.randrange(len(valores))], naipes[random.randrange(len(naipes))])

            # Adiciona na lista
            cartas.append(mudaNome(cartaNova))

            # Gera pontuação
            pontuacao += baralho21(cartaNova,cartas,pontuacao)[0]

    # CPU
    cartasCPU = []
    pontuacaoCPU = 0

    # Cartas da CPU
    while len(cartasCPU) <= 5 and pontuacaoCPU < 17 and pontuacao != 21:
        cartaNova = (valores[random.randrange(len(valores))], naipes[random.randrange(len(naipes))])

        # Valida a carta
        while not validaCartaCPU(cartaNova,cartas,cartasCPU):
            cartaNova = (valores[random.randrange(len(valores))], naipes[random.randrange(len(naipes))])

        # Adiciona na lista
        cartasCPU.append(mudaNome(cartaNova))

        # Gera pontuação
        pontuacaoCPU += baralho21CPU(cartaNova, pontuacaoCPU)[0]

    # Resultado
    if pontuacaoCPU > 21:
        resultado = "Ganhou"
    elif pontuacao < 22 and pontuacao >= pontuacaoCPU:
        resultado = "Ganhou"
    else:
        resultado = "Perdeu"
    print("\nCartas Você:",cartas,"\nTotal de pontos:",pontuacao,"\nCartas CPU:",cartasCPU,"\nPontuação CPU:",pontuacaoCPU,"\nResultado:",resultado)

# Principal
print("\nGame de Baralho\n")

valores = (1,2,3,4,5,6,7,8,9,10,11,12,13)

naipes = ("♣", "♥", "♠", "♦")

# Menu
menu = 0
while menu != 1 and menu != 2:
    try:
        menu = int(input("1 - Maior Carta\n2 - Blackjack(21)\nEscolha o jogo que deseja: "))
    except:
        print("\nDigite apenas números!\n")
        menu = 0
    if menu == 1:
        maiorCarta(valores, naipes)
    elif menu == 2:
        blackjack(valores, naipes)