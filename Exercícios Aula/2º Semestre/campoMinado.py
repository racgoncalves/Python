
import random

# <<<<<< FUNÇÕES >>>>>>

# Função que cria a matriz do campo minado
def criaMatriz(linhas,colunas):
    matriz = []

    i = 0
    while i < linhas:
        matriz.append([0] * colunas)
        i += 1

    return matriz

# Função que cria a matrix oculta para o jogador
def criaMatrizOculta(linhas,colunas):
    matriz = []

    i = 0
    while i < linhas:
        matriz.append(['X'] * colunas)
        i += 1

    return matriz

# Função que coloca as bombas na matriz
def colocarBombas(matriz,bombas):

   while len(bombas) != 0:
    i = random.randrange(0,10)
    j = random.randrange(0,10)
    if matriz[i][j] != -1:
        matriz[i][j] = bombas.pop()

# Função que preenche os números em volta da bomba
def preencheMatriz(matriz):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[0]):
            if matriz[i][j] == -1:

                # Baixo
                if i+1 < len(matriz) and matriz[i+1][j] != -1:
                    matriz[i+1][j] += 1
                # Diagonal Baixo e Direita
                if i+1 < len(matriz) and j+1 < len(matriz[0]) and matriz[i+1][j+1] != -1:
                    matriz[i+1][j+1] += 1
                # Direita
                if j+1 < len(matriz[0]) and matriz[i][j+1] != -1:
                    matriz[i][j+1] += 1
                # Cima
                if i-1 >= 0 and matriz[i-1][j] != -1:
                    matriz[i-1][j] += 1
                # Diagonal Cima e Esquerda
                if i-1 >= 0 and j-1 >= 0 and matriz[i-1][j-1] != -1:
                    matriz[i-1][j-1] += 1
                # Esquerda
                if j-1 >= 0 and matriz[i][j-1] != -1:
                    matriz[i][j-1] += 1
                # Diagonal Baixo e Esquerda
                if i+1 < len(matriz) and j-1 >= 0 and matriz[i+1][j-1] != -1:
                    matriz[i+1][j-1] += 1
                # Diagonal Cima e Direita
                if i-1 > 0 and j+1 < len(matriz[0]) and matriz[i-1][j+1] != -1:
                    matriz[i-1][j+1] += 1
            j += 1
        i += 1

# Função que expande o campo caso seja 0 o valor da posição
def expandeZero(matriz, matrizOculta, linha, coluna):

    i = linha
    j = coluna

    # Baixo
    if i + 1 < len(matriz) and matriz[i + 1][j] >= 0 and matrizOculta[i + 1][j] == 'X':
        matrizOculta[i + 1][j] = matriz[i + 1][j]
        if matriz[i + 1][j] == 0:
            expandeZero(matriz, matrizOculta, i + 1, j)

    # Diagonal Baixo e Direita
    if i + 1 < len(matriz) and j + 1 < len(matriz[0]) and matriz[i + 1][j + 1] >= 0 and matrizOculta[i + 1][j + 1] == 'X':
        matrizOculta[i + 1][j + 1] = matriz[i + 1][j + 1]
        if matriz[i + 1][j + 1] == 0:
            expandeZero(matriz, matrizOculta, i + 1, j + 1)

    # Direita
    if j + 1 < len(matriz[0]) and matriz[i][j + 1] >= 0 and matrizOculta[i][j + 1] == 'X':
        matrizOculta[i][j + 1] = matriz[i][j + 1]
        if matriz[i][j + 1] == 0:
            expandeZero(matriz, matrizOculta, i, j + 1)

    # Cima
    if i - 1 >= 0 and matriz[i - 1][j] >= 0 and matrizOculta[i - 1][j] == 'X':
        matrizOculta[i - 1][j] = matriz[i - 1][j]
        if matriz[i - 1][j] == 0:
            expandeZero(matriz, matrizOculta, i - 1, j)

    # Diagonal Cima e Esquerda
    if i - 1 >= 0 and j - 1 >= 0 and matriz[i - 1][j - 1] >= 0 and matrizOculta[i - 1][j - 1] == 'X':
        matrizOculta[i - 1][j - 1] = matriz[i - 1][j - 1]
        if matriz[i - 1][j - 1] == 0:
            expandeZero(matriz, matrizOculta, i - 1, j - 1)

    # Esquerda
    if j - 1 >= 0 and matriz[i][j - 1] >= 0 and matrizOculta[i][j - 1] == 'X':
        matrizOculta[i][j - 1] = matriz[i][j - 1]
        if matriz[i][j - 1] == 0:
            expandeZero(matriz, matrizOculta, i, j - 1)

    # Diagonal Baixo e Esquerda
    if i + 1 < len(matriz) and j - 1 >= 0 and matriz[i + 1][j - 1] >= 0 and matrizOculta[i + 1][j - 1] == 'X':
        matrizOculta[i + 1][j - 1] = matriz[i + 1][j - 1]
        if matriz[i + 1][j - 1] == 0:
            expandeZero(matriz, matrizOculta, i + 1, j - 1)

    # Diagonal Cima e Direita
    if i - 1 > 0 and j + 1 < len(matriz[0]) and matriz[i - 1][j + 1] >= 0 and matrizOculta[i - 1][j + 1] == 'X':
        matrizOculta[i - 1][j + 1] = matriz[i - 1][j + 1]
        if matriz[i - 1][j + 1] == 0:
            expandeZero(matriz, matrizOculta, i - 1, j + 1)

# Função que checa se o jogador ganhou
def checaVitoria(matrizOculta):

    cont = 0

    for i in range(len(matrizOculta)):
        for j in range(len(matrizOculta[0])):
            if matrizOculta[i][j] == 'X': cont += 1

    if cont == 10: return True

# Função que realiza a jogada
def jogada(matriz,matrizOculta,linha,coluna,):

    if matriz[linha][coluna] == -1:
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j] == -1: matrizOculta[i][j] = matriz[i][j]
        return False

    elif checaVitoria(matrizOculta) == True:
        return True

    elif matriz[linha][coluna] > 0:
        matrizOculta[linha][coluna] = matriz[linha][coluna]

    elif matriz[linha][coluna] == 0:
        matrizOculta[linha][coluna] = matriz[linha][coluna]
        expandeZero(matriz, matrizOculta, linha, coluna)

# Função que imprime a matriz
def imprimeMatriz(matriz):
    for linha in matriz:
        print(linha)

# <<<<<< FIM DAS FUNÇÕES >>>>>>>

# Monta o jogo
campo = criaMatriz(10,10)
matrizOculta = criaMatrizOculta(10,10)
bombas = [-1] * 10
colocarBombas(campo,bombas)
preencheMatriz(campo)

# Inicia o jogo
linha = 10
coluna = 10

while linha < 0 or linha > 9:
    try:
        linha = int(input("\nDigite a posiçao da linha: "))
        if linha < 0 or linha > 9: print("\nValor inválido, digite entre 0 e 9!")
    except:
        print("\nDigite apenas números!")
        linha = 10

while coluna < 0 or coluna > 9:
    try:
        coluna = int(input("\nDigite a posiçao da coluna: "))
        if coluna < 0 or coluna > 9: print("\nValor inválido, digite entre 0 e 9!")
    except:
        print("\nDigite apenas números!")
        coluna = 10

# Looping do jogo
while jogada(campo,matrizOculta,linha,coluna) != False and jogada(campo,matrizOculta,linha,coluna) != True:

    print("")
    imprimeMatriz(matrizOculta)

    repeticao = True

    while repeticao == True:

        linha = 10
        coluna = 10

        while linha < 0 or linha > 9:
            try:
                linha = int(input("\nDigite a posiçao da linha: "))
                if linha < 0 or linha > 9: print("\nValor inválido, digite entre 0 e 9!")
            except:
                print("\nDigite apenas números!")
                linha = 10

        while coluna < 0 or coluna > 9:
            try:
                coluna = int(input("\nDigite a posiçao da coluna: "))
                if coluna < 0 or coluna > 9: print("\nValor inválido, digite entre 0 e 9!")
            except:
                print("\nDigite apenas números!")
                coluna = 10

        if matrizOculta[linha][coluna] == 'X': repeticao = False
        else: print("\nEsta posição já foi escolhida!")

# Resultado do jogo
print("")

if jogada(campo,matrizOculta,linha,coluna) == False:
    imprimeMatriz(matrizOculta)
    print("\nVocê explodiu =/")

else:
    imprimeMatriz(campo)
    print("\nVocê ganhou \o/")

# Fim do programa