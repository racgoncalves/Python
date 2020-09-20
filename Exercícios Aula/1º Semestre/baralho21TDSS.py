import baralhoTDSS
import random

def compra(baralho):
    #sortear um número aleatorio entre 0 e 51
    #retorna a carta que se encontra nesta posicao
    pos = random.randint(0, 51)
    return baralho[pos]

def valor(carta):
    if carta[0] > 10:
        return 10
    else:
        return carta[0]

deck = baralhoTDSS.getBaralho()

suaPontuacao = 0
cpuPontuacao = 0

#VOCE RECEBENDO CARTAS
card = compra(deck)
suaPontuacao = suaPontuacao + valor(card) #valor da carta
aux = baralhoTDSS.imprimeCarta(card)
print(aux)

card = compra(deck)
suaPontuacao = suaPontuacao + valor(card) #valor da carta
aux = baralhoTDSS.imprimeCarta(card)
print(aux)
print(suaPontuacao)

#CPU recebendo cartas
card = compra(deck)
cpuPontuacao = cpuPontuacao + valor(card)
card = compra(deck)
cpuPontuacao = cpuPontuacao + valor(card)

resp = input("Deseja mais cartas (S/N)?")
while resp == 'S' and suaPontuacao < 21:
    card = compra(deck)
    aux = baralhoTDSS.imprimeCarta(card)
    print(aux)
    suaPontuacao = suaPontuacao + valor(card)
    print("Pontos: ", suaPontuacao)
    resp = input("Deseja mais cartas (S/N)? ")


while cpuPontuacao < 16:
    card = compra(deck)
    cpuPontuacao = cpuPontuacao + valor(card)


if suaPontuacao > 21 and cpuPontuacao > 21:
    print("Ambos perderam!")
elif suaPontuacao > 21 or suaPontuacao < cpuPontuacao:
    print("CPU venceu")
elif cpuPontuacao > 21 or cpuPontuacao < suaPontuacao: 
    print("Você venceu")
#elif cpuPontuacao < suaPontuacao:
#    print("Você venceu")
#elif suaPontuacao < cpuPontuacao:
#    print("CPU venceu")
else:
    print("Deu empate")

print("Seus pontos: ", suaPontuacao)
print("CPU pontos: ", cpuPontuacao)                
