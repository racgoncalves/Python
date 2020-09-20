def imprimeCarta(carta):
    if carta[0] == 1:
        return "A" + carta[1]
    elif carta[0] == 11:
        return "J" + carta[1]
    elif carta[0] == 12:
        return "Q" + carta[1]
    elif carta[0] == 13:
        return "K" + carta[1]    
    else:    
        return str(carta[0]) + carta[1]

def imprimeMao(colecao):
    resp = ""
    for c in colecao:
        resp = resp + " " + imprimeCarta(c)

    return resp    

#retorna um baralho
def getBaralho():
    ases = ((1, "♣"), (1, "♥"), (1, "♠"), (1, "♦"))
    dois = ((2, "♣"), (2, "♥"), (2, "♠"), (2, "♦"))
    tres = ((3, "♣"), (3, "♥"), (3, "♠"), (3, "♦"))
    quatro = ((4, "♣"), (4, "♥"), (4, "♠"), (4, "♦"))
    cinco = ((5, "♣"), (5, "♥"), (5, "♠"), (5, "♦"))
    seis = ((6, "♣"), (6, "♥"), (6, "♠"), (6, "♦"))
    sete = ((7, "♣"), (7, "♥"), (7, "♠"), (7, "♦"))
    oito = ((8, "♣"), (8, "♥"), (8, "♠"), (8, "♦"))
    nove = ((9, "♣"), (9, "♥"), (9, "♠"), (9, "♦"))
    dez = ((10, "♣"), (10, "♥"), (10, "♠"), (10, "♦"))
    valete = ((11, "♣"), (11, "♥"), (11, "♠"), (11, "♦"))
    dama = ((12, "♣"), (12, "♥"), (12, "♠"), (12, "♦"))
    rei = ((13, "♣"), (13, "♥"), (13, "♠"), (13, "♦"))
    return ases + dois + tres + quatro + cinco + seis + sete + oito + nove + dez + valete + dama + rei


#mao = getBaralho()
#for c in mao:
#    print(imprimeCarta(c))


