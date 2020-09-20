def criaTabuleiro():
    tab = []
    for i in range(3):
        tab.append([' '] * 3)
    return tab

def imprime(tab):
    for lin in tab:
        print(lin)

def temEspaco(tab):
    for i in range(3):
        for j in range(3):
            if tab[i][j] == ' ':
                return True
    return False

def haGanhador(tab):
    for i in range(3):
        #checando as linhas
        if tab[i][0]!=' ' and tab[i][0]==tab[i][1] and tab[i][1]==tab[i][2]:
            return True
        #checando as colunas    
        if tab[0][i]!=' ' and tab[0][i]==tab[1][i] and tab[1][i]==tab[2][i]:
            return True

    #diagonal principal
    if tab[0][0]!=' ' and tab[0][0]==tab[1][1] and tab[1][1]==tab[2][2]:
        return True
        
    if tab[0][2]!=' ' and tab[0][2]==tab[1][1] and tab[1][1]==tab[2][0]:
        return True

    return False

def joga(tab, l, c, jogador):
    tab[l][c] = jogador

def trocaJogador(jogador):
    if jogador == 'X':
        return 'O'
    else:
        return 'X'    

matriz = criaTabuleiro()
player = 'X'

while temEspaco(matriz) and not haGanhador(matriz):
    imprime(matriz)
    print("Jogador", player)
    lin = int(input("Informe a linha: "))
    col = int(input("Informe a coluna: "))
    joga(matriz, lin, col, player)
    player = trocaJogador(player)

if haGanhador(matriz):
    print("Ganhador: ", trocaJogador(player))
    imprime(matriz)
else:
    print("Empatou!")
        



